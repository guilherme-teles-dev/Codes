import sounddevice as sd
import numpy as np
import threading
import time
import sys

# --- DEFINIÇÃO DOS EFETOS ---
# Cada função recebe o sinal (numpy array) e a taxa de amostragem fs e retorna o sinal processado.

def bypass(signal, fs):
    # Sem efeito, apenas retorna o sinal inalterado.
    return signal

def equalize_fft(signal, fs, gain_low=1.5, gain_mid=0.8, gain_high=1.0):
    # Aplica equalização via FFT: ajusta ganhos para faixas de baixa, média e alta frequência.
    fft_data = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(len(signal), d=1/fs)
    low = freqs < 300
    mid = (freqs >= 300) & (freqs < 3000)
    high = freqs >= 3000
    fft_data[low] *= gain_low
    fft_data[mid] *= gain_mid
    fft_data[high] *= gain_high
    return np.fft.irfft(fft_data, n=len(signal))

def butter_lowpass_filter(signal, cutoff, fs, order=5):
    from scipy.signal import butter, lfilter
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return lfilter(b, a, signal)

def echo(signal, fs, delay_time=0.3, decay=0.6):
    # Aplica um delay simples: soma o sinal com uma versão atrasada.
    delay_samples = int(delay_time * fs)
    output = np.zeros(len(signal))
    # Copia o sinal original e soma o sinal atrasado multiplicado pelo decay
    output[:len(signal)] = signal
    if delay_samples < len(signal):
        output[delay_samples:] += decay * signal[:-delay_samples]
    return output

def reverb(signal, fs, ir_duration=0.001):
    # Aplica reverb simples via convolução com uma resposta ao impulso exponencial.
    from scipy.signal import fftconvolve
    ir_length = int(fs * ir_duration)
    impulse_response = np.exp(-np.linspace(0, 5, ir_length))
    return fftconvolve(signal, impulse_response, mode='same')

def pitch_shift(signal, fs, n_steps=4):
    # Exemplo utilizando a biblioteca librosa para alterar o pitch.
    import librosa
    # Librosa trabalha com float32
    signal = signal.astype(np.float32)
    shifted = librosa.effects.pitch_shift(signal, sr=fs, n_steps=n_steps)
    return shifted

def noise_gate(signal, threshold=0.05):
    # Zera as amplitudes abaixo do limiar.
    return np.where(np.abs(signal) < threshold, 0, signal)

def compressor(signal, threshold=0.3, ratio=4):
    # Compressão simples: reduz a variação acima de um certo limiar.
    compressed = np.copy(signal)
    over = np.abs(signal) > threshold
    compressed[over] = np.sign(signal[over]) * (threshold + (np.abs(signal[over]) - threshold) / ratio)
    return compressed

def distortion(signal, gain=10, clipping_threshold=0.8):
    # Aplica ganho e em seguida clipe os valores para criar efeito de distorção.
    amplified = signal * gain
    return np.clip(amplified, -clipping_threshold, clipping_threshold)

def flanger(signal, fs, max_delay=0.003, lfo_freq=0.25, mix=0.5):
    # Aplica flanger: mistura o sinal original com uma versão atrasada cujo atraso varia com um LFO.
    n_samples = len(signal)
    output = np.zeros(n_samples)
    lfo = max_delay * fs * (0.5 * (1 + np.sin(2 * np.pi * lfo_freq * np.arange(n_samples)/fs)))
    for n in range(n_samples):
        delay = int(lfo[n])
        if n - delay >= 0:
            output[n] = (1 - mix) * signal[n] + mix * signal[n - delay]
        else:
            output[n] = signal[n]
    return output

# --- MAPEAMENTO DOS EFETOS ---
# Cada entrada é uma tupla (nome do efeito, função de processamento)
effects = {
    '0': ('Bypass (Sem Efeito)', bypass),
    '1': ('Echo', echo),
    '2': ('Distortion', distortion),
    '3': ('Reverb', reverb),
    '4': ('Equalização (FFT)', equalize_fft),
    '5': ('Filtro Passa-Baixa', lambda s, fs: butter_lowpass_filter(s, cutoff=300, fs=fs, order=5)),
    '6': ('Noise Gate', noise_gate),
    '7': ('Compressor', compressor),
    '8': ('Flanger', flanger)
    # Você pode adicionar mais efeitos se desejar.
}

# Variável global que define o efeito atual (inicialmente sem efeito)
current_effect = '0'

# --- FUNÇÃO DE LISTENING PARA O TECLADO ---
def keyboard_listener():
    global current_effect
    print("Alternância de efeitos: pressione a tecla correspondente para mudar o efeito.")
    for key, (name, _) in effects.items():
        print(f"{key}: {name}")
    print("Pressione 'q' para sair.")
    while True:
        key = input("Escolha efeito: ").strip()
        if key == 'q':
            print("Encerrando o programa...")
            sys.exit(0)
        if key in effects:
            current_effect = key
            print(f"Efeito atual: {effects[current_effect][0]}")
        else:
            print("Tecla inválida. Tente novamente.")

# --- FUNÇÃO CALLBACK DO STREAM DE ÁUDIO ---
def audio_callback(indata, outdata, frames, time_info, status):
    if status:
        print(status)
    # Copia o sinal de entrada
    processed = np.copy(indata)
    # Aplica o efeito escolhido (supondo sinal mono: shape (frames, 1))
    # Caso o efeito necessite de parâmetros adicionais, usamos os valores padrão definidos nas funções.
    effect_func = effects[current_effect][1]
    # Tente processar o bloco; se o efeito, por exemplo, alterar o tamanho do array,
    # recorte para manter a consistência com a saída.
    processed_block = effect_func(processed[:, 0], fs)
    if len(processed_block) < frames:
        # Caso o sinal processado seja menor (por exemplo, pitch shifting pode alterar tamanho),
        # preencha com zeros.
        processed_block = np.pad(processed_block, (0, frames - len(processed_block)))
    # Atualiza o outdata (colocando o sinal processado na coluna 0)
    outdata[:, 0] = processed_block

# --- CONFIGURAÇÃO DO STREAM DE ÁUDIO ---
fs = 44100       # taxa de amostragem
blocksize = 1024 # tamanho do bloco (em samples)

# Inicia o listener de teclado em uma thread separada (daemon para que encerre com o programa)
listener_thread = threading.Thread(target=keyboard_listener, daemon=True)
listener_thread.start()

print("Iniciando stream de áudio. Você pode alternar os efeitos via teclado.")

# Inicia o stream de áudio; o callback será chamado a cada bloco de áudio capturado.
with sd.Stream(channels=1, samplerate=fs, blocksize=blocksize, callback=audio_callback):
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Encerrando stream de áudio...")

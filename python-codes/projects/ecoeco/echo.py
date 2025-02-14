def add_delay(signal, fs, delay_time=0.5, decay=0.5):
    delay_samples = int(delay_time * fs)
    # Cria um array com zeros para armazenar o sinal atrasado
    delayed_signal = np.zeros(len(signal) + delay_samples)
    delayed_signal[:len(signal)] += signal
    delayed_signal[delay_samples:] += decay * signal
    # Retorna com o mesmo tamanho do sinal original
    return delayed_signal[:len(signal)]

# Exemplo de uso:
delayed_signal = add_delay(signal, fs, delay_time=0.3, decay=0.6)

plt.figure()
plt.plot(t, signal, label="Original")
plt.plot(t, delayed_signal, label="Com Delay")
plt.legend()
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.title("Efeito de Delay/Echo")
plt.show()

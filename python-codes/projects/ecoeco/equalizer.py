import sounddevice as sd
import numpy as np

def apply_equalizer(data):
    # Aumentar graves (exemplo simplificado)
    transformed_data = data * np.array([1.5, 1.5])  # Ajuste de canal esquerdo/direito
    return transformed_data

def callback(indata, outdata, frames, time, status):
    # Processa os dados de entrada e escreve no array de saída
    outdata[:] = apply_equalizer(indata)

# Configurar stream com processamento
with sd.Stream(channels=2, callback=callback):
    input("Pressione Enter para parar...")

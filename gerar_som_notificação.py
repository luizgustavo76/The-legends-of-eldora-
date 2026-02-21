import numpy as np
import soundfile as sf

sr = 48000  # taxa de amostragem alta
dur = 0.6   # duração total da "gota"

t = np.linspace(0, dur, int(sr*dur), endpoint=False)

# base: seno suave com modulação sutil
freq_base = 400
freq_mod = 3
som = np.sin(2*np.pi*freq_base*t + 0.5*np.sin(2*np.pi*freq_mod*t))

# harmônicos sutis
som += 0.2*np.sin(2*np.pi*freq_base*2*t + 0.1*np.sin(2*np.pi*freq_mod*2*t))
som += 0.1*np.sin(2*np.pi*freq_base*3*t + 0.1*np.sin(2*np.pi*freq_mod*3*t))

# envelope natural
env = np.exp(-5*t) * (1 - np.exp(-10*t))
som *= env

# pequenas gotas secundárias
for i in [0.15, 0.32, 0.48]:
    start = int(sr*i)
    length = int(sr*0.12)
    drop = np.sin(2*np.pi*(freq_base+150)*np.linspace(0, 0.12, length))
    drop *= np.exp(-12*np.linspace(0, 0.12, length))
    som[start:start+length] += drop

# normaliza
som /= np.max(np.abs(som))

# salva em 32-bit float, compatível com praticamente tudo
sf.write("gota32bit.wav", som.astype('float32'), sr, subtype='FLOAT')

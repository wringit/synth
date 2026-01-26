import numpy as np
from scipy.io import wavfile
def build(song, fname="temp.wav", amp=0.1, sample_rate=44100):
    song = stack(song,amp)
    wavfile.write(fname,sample_rate,song)

def stack(voices,amp):
    hdized = []
    for x in range(len(voices)):
        wave = np.array(voices[x])
        hdized = hdized + [np.int16(wave*amp*(2**15-1))]
    return np.stack(hdized).T
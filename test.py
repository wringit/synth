import math
from tkinter import *
import numpy as np
from scipy.io import wavfile
#from functools import reduce
# Amplitude = volume
# Phase constant = starting angle

#Pressure on air?

def wav_to_file(waves, fname="temp.wav", amp=0.1, sample_rate=44100):

    hdized = []
    for x in range(len(waves)):
        wave = np.array(waves[x])
        hdized = hdized + [np.int16(wave*amp*(2**15-1))]
        #hdized[x] = wave
    
    #wave2 = np.array(waves[1])
    #wave2 = np.int16(wave2*amp*(2**15-1))
    wave = np.stack(hdized).T #idk wtf t does
    #wave = np.stack([wave,wave2]).T
    print(wave)
    wavfile.write(fname,sample_rate,wave)

def sin_oscillation(freq, amp, phi=0, sample_rate=44100):
    om = math.tau*freq # tau=2pi
    phi = phi/360.0*math.tau
    theta = 0.0
    while True:
        yield amp*math.sin(theta+phi)
        theta += om/sample_rate

def tri_oscillation(freq, amp, phi=0, sample_rate=44100):
    om = math.tau * freq
    phi = phi / 360.0 * math.tau
    theta = 0.0
    while True:
                # Triangle wave: ranges from -1 to 1, changes direction at 0 and pi
        normalized = (theta + phi) % math.tau
        if normalized < math.pi:
            value = 2.0 * (normalized / math.pi) - 1.0
        else:
            value = 2.0 * (1.0 - (normalized - math.pi) / math.pi) - 1.0
        yield amp * value
        theta += om/sample_rate
def square_oscillation(freq, amp, phi=0, sample_rate=44100):
    om = math.tau * freq
    phi = phi / 360.0 * math.tau
    theta = 0.0
    while True:
        normalized = (theta + phi) % math.tau
        yield amp if normalized < math.pi else -amp
        theta += om / sample_rate
def sawtooth_oscillation(freq, amp, phi=0, sample_rate=44100):
    om = math.tau * freq
    phi = phi / 360.0 * math.tau
    theta = 0.0
    while True:
        normalized = (theta + phi) % math.tau
        yield amp * (2 * normalized / math.tau - 1)
        theta += om / sample_rate
sin_gen_a = sawtooth_oscillation(440,0.4)
sin_gen_e = sawtooth_oscillation(660,0.4)
sin_gen_c = sawtooth_oscillation(523,0.4)

wav_to_file([[next(sin_gen_a) for i in range(44100*10)],[next(sin_gen_c) for i in range(44100*10)],[next(sin_gen_e) for i in range(44100*10)]],amp=0.4)
# root = Tk()
# root.title("Sin Wave Oscillation")
            
# canvas = Canvas(root, width=800, height=400, bg='white')
# canvas.pack()
# def plot_sin_wave(freq,amp):

            
#     #freq = 100
#     #amp = 100.0
#     phi = 0.0
#     sample_rate = 44100
            
#     gen = sin_oscillation(freq, amp, phi, sample_rate)
#     points = []
            
#     for i in range(800):
#         y = next(gen)
#         points.append((i, 200 - y))
            
#     for i in range(len(points) - 1):
#         canvas.create_line(points[i][0], points[i][1], 
#                                   points[i+1][0], points[i+1][1], fill='blue')
            
#     root.mainloop()

#plot_sin_wave(440,100.0)
#plot_sin_wave(554,100.0)
#plot_sin_wave(660,100.0)

# osc = sin_oscillation(5,500000000000,0,1)
# for x in range(500):
#     print(f"{x}: {next(osc)}")
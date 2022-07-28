import soundfile as sf
from scipy import signal
import numpy as np
from numpy.polynomial import Polynomial as P

def mylfilt(x, a, b):
    return np.array(P(b)//P(a))*x

#read .wav file 
input_signal,fs = sf.read('Sound_Noise.wav') 

#sampling frequency of Input signal
sampl_freq=fs

#order of the filter
order=4   

#cutoff frquency 4kHz
cutoff_freq=4000.0  

#digital frequency
Wn=2*cutoff_freq/sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 
print(b)
print(a)

#filter the input signal with butterworth filter
output_signal = signal.filtfilt(b, a, input_signal)
output_signal_1 = signal.lfilter(b, a, input_signal)
print(output_signal_1[:10])
print(mylfilt(input_signal[:10], a, b))

#write the output signal into .wav file
sf.write('Sound_With_ReducedNoise.wav', output_signal, fs) 

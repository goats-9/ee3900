import numpy as np
from matplotlib import pyplot as plt
import os

f = 50
V = 5
A = 12
N = 100
l = 5
t = np.linspace(-l, l, N)
s1 = np.sinc(t)
s2 = A*np.abs(np.sin(2*np.pi*f*t))
sc = np.convolve(s1, s2, mode='full')
plt.plot(np.linspace(-2*l, 2*l, 2*N - 1), V*sc/sc[N])
plt.grid()
plt.xlabel('t (s)')
plt.ylabel('V')
plt.savefig('../figs/4_3.png')
os.system('sh gopen.sh ../figs/4_3.png')

import numpy as np
from scipy.fft import fft, ifft
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def nlgn(n, a): return a*n*np.log2(n)

a = 2**(np.arange(20))
a1 = np.loadtxt('fft.txt', dtype='double')
a2 = np.loadtxt('ifft.txt', dtype='double')

popt, pcov = curve_fit(nlgn, a, a2)
a2pred = nlgn(a, *popt)
#plots
plt.plot(a, a1, 'o')
plt.plot(a, a2, 'o')
plt.plot(a, a2pred)
plt.legend(["Simulation (FFT)", "Simulation (IFFT)", "Analysis"])
plt.xlabel('n')
plt.ylabel('T(n) (ms)')
plt.grid()# minor

#If using termux
plt.savefig('../figs/6_7_1.png')
#subprocess.run(shlex.split("termux-open ../figs/yndft.pdf"))
#else
#plt.show()

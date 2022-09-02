import numpy as np
from scipy.fft import fft, ifft
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def nsq(n, a): return a*n*n

x = np.arange(1e3 - 1)
a3 = np.loadtxt('conv.txt', dtype='double')
popt, pcov = curve_fit(nsq, x, a3)
a3pred = nsq(x, *popt)
#plots
plt.plot(x, a3, '.')
plt.plot(x, a3pred)
plt.xlabel('n')
plt.ylabel('T(n) (s)')
plt.legend(["Simulation (convolution)", "Analysis"])
plt.grid()# minor

#If using termux
plt.savefig('../figs/6_7_2.png')
#subprocess.run(shlex.split("termux-open ../figs/yndft.pdf"))
#else
#plt.show()

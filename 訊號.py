import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,25.12,0.0001)
def anser():
    m = 1
    y1 = 0
    for i in range(1,20):
        y = ((-1)**(i+1))*(4*m/((2*i-1)*np.pi))*np.cos(m*(2*i-1)*t)
        y1 = y+y1

    plt.plot(t,y1,'red',linewidth = 2.0)
    plt.title('Fourier Series',fontsize=20)
    plt.xlabel('Time',fontsize=20)
    plt.ylabel('Amplitude',fontsize=20)
    plt.xlim(0,25.12)
    plt.show()

anser()



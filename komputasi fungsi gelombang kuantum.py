import matplotlib.pyplot as plt
import numpy as np

#computation of the function quantum
a = 2 *(0.529 * 10**(-10)) #m
m = 9.109 * 10**(-31) #kg mass of the electron
h = 6.626 * 10**(-34)/ (2*np.pi) #J.s Planck constant
x = np.linspace(0, a, 1000)
E = np.zeros(3)
psi = np.zeros((3, len(x)))
figure, axis = plt.subplots(3,1)
for n in range(1,4):
    E[n-1] = ((n**2) * ((np.pi)**2) * (h**2))/((2 * m * (a**2))) * (6.242*10**18)
    for i in range(len(x)):
        psi[n-1, i] = (np.sqrt(np.pi/a) * np.sin(n * np.pi * x[i]/a))**2
    axis[n-1].plot(x / a, psi[n-1], color = 'red', linewidth = 2)
    axis[n-1].set_title(' E = %0.1i' % E[n-1] + ' eV')
    axis[n-1].grid(True)
    axis[n-1].set_xlabel('x (m)')
    axis[n-1].set_ylabel('psi')



plt.show()

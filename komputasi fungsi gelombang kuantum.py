import matplotlib.pyplot as plt
import numpy as np

#computation of the function quantum
a = 2 *(0.529 * 10**(-10)) #m
m = 9.109 * 10**(-31) #kg mass of the electron
h = 6.626 * 10**(-34) #J.s Planck constant
x = np.linspace(0, a, 1000)
E = np.zeros(3)
psi = np.zeros((3, len(x)))
for n in range(1,4):
    E[n-1] = (n**2 * np.pi**2 * h**2)/(2 * m * a**2)/1.6*10**(-19)
    for i in range(len(x)):
        psi[n-1, i] = (np.sqrt(np.pi/a) * np.sin(n * np.pi * x[i]/a))**2
plt.plot(x/a,psi[0], label = 'n = 1')
plt.plot(x/a,psi[1], label = 'n = 2')
plt.plot(x/a,psi[2], label = 'n = 3')
plt.xlabel('x (m)')
plt.ylabel('ψ(x)')
plt.legend()
plt.show()
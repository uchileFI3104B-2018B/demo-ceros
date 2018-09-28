"""
Resuelve la ecuacion sin(x) = cos(x) entre 0 y pi.
Utiliza el metodo de la biseccion.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect, newton, brentq


x_to_plot = np.linspace(0, np.pi, 100)


plt.clf()
plt.plot(x_to_plot, np.sin(x_to_plot), label="seno(x)")
plt.plot(x_to_plot, np.cos(x_to_plot), label="cos(x)")

plt.xlabel("x [radianes]")



def seno_menos_coseno(x):
    """x en radianes.
    """
    output = np.sin(x) - np.cos(x)
    return output

def biseccion(func, a, b, tol=1e-4):
    """
    Busca un cero usando el metodo de la biseccion
    ...
    """
    p = (a + b) / 2 
    while np.fabs(func(p)) > tol:
        p = (a + b) / 2
        if func(a) * func(p) < 0:
            b = p
        elif func(a) * func(p) > 0:
            a = p
        else:
            return p
    return p

cero_biseccion = biseccion(seno_menos_coseno, 0., 2., tol=1e-7)
cero_scipy_bisect = bisect(seno_menos_coseno, 0., 2., rtol=1e-7)
cero_scipy_newton = newton(seno_menos_coseno, 2.)
cero_scipy_brent = brentq(seno_menos_coseno, 0., 2.)

plt.axvline(cero_biseccion, color='r', label='cero_biseccion')
plt.legend()
# plt.savefig('cero_biseccion.png')
plt.show()
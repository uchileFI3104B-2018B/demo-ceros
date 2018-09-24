"""
Resuelve la ecuacion sin(x) = cos(x) entre 0 y pi.
Utiliza el metodo de la biseccion.
"""

import numpy as np
import matplotlib.pyplot as plt


x_to_plot = np.linspace(0, np.pi, 10)


plt.clf()
plt.plot(x_to_plot, np.sin(x_to_plot), label="seno(x)")
plt.plot(x_to_plot, np.cos(x_to_plot), label="cos(x)")

plt.xlabel("x [radianes]")
plt.legend()

plt.show()
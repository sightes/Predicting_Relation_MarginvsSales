# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import matplotlib.pyplot as plt

def euler_explicito(f, y0, t):
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        dt = t[i] - t[i - 1]
        y[i] = y[i - 1] + f(y[i - 1], t[i - 1]) * dt
    return y

# Ejemplo de uso
def modelo(y, t):
    k = 0.3
    dydt = -k * y
    return dydt

y0 = 5
t = np.linspace(0, 20, 100)

solucion = euler_explicito(modelo, y0, t)

# Graficar la solución
plt.plot(t, solucion, label='Aproximación Euler Explícito')
plt.xlabel('Tiempo')
plt.ylabel('y(t)')
plt.title('Método de Euler Explícito')
plt.legend()
plt.show()

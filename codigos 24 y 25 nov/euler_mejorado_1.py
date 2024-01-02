# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import matplotlib.pyplot as plt

def euler_mejorado(f, y0, t):
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        dt = t[i] - t[i - 1]
        k1 = f(y[i - 1], t[i - 1])
        k2 = f(y[i - 1] + k1 * dt, t[i])
        y[i] = y[i - 1] + (k1 + k2) * dt / 2
    return y

# Ejemplo de uso
def modelo(y, t):
    k = 0.3
    dydt = -k * y
    return dydt

y0 = 5
t = np.linspace(0, 20, 100)

solucion = euler_mejorado(modelo, y0, t)

# Graficar la solución
plt.plot(t, solucion, label='Aproximación Euler Mejorado')
plt.xlabel('Tiempo')
plt.ylabel('y(t)')
plt.title('Método de Euler Mejorado (Heun)')
plt.legend()
plt.show()

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función f(t, y)
def f(t, y):
    return -2 * t * y**2

# Condiciones iniciales
t0 = 0
y0 = 1
tf = 2  # Tiempo final
h = 0.1  # Paso de tiempo

# Método de Euler
t = np.arange(t0, tf + h, h)  # Incluye tf en el arreglo
y = np.zeros(len(t))
y[0] = y0

for i in range(1, len(t)):
    y[i] = y[i - 1] + h * f(t[i - 1], y[i - 1])

# Visualización
plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y')
plt.title('Solución de EDO usando Método de Euler')
plt.grid(True)
plt.show()

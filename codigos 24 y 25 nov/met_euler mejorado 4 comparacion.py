# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función f(t, y)
def f(t, y):
    return -2 * t * y**2

# Método de Euler
def euler(f, t0, y0, h, tf):
    t = np.arange(t0, tf + h, h)  # Incluye tf en el arreglo
    y = np.zeros(len(t))
    y[0] = y0

    for i in range(1, len(t)):
        y[i] = y[i - 1] + h * f(t[i - 1], y[i - 1])
    
    return t, y

# Método de Euler Mejorado (Heun)
def euler_mejorado(f, t0, y0, h, tf):
    t = np.arange(t0, tf + h, h)
    y = np.zeros(len(t))
    y[0] = y0

    for i in range(1, len(t)):
        y_pred = y[i - 1] + h * f(t[i - 1], y[i - 1])
        y[i] = y[i - 1] + h * (f(t[i - 1], y[i - 1]) + f(t[i], y_pred)) / 2
    
    return t, y

# Condiciones iniciales
t0 = 0
y0 = 1
tf = 10  # Tiempo final
h = 0.1  # Paso de tiempo

# Aplicar los métodos
t, y_euler = euler(f, t0, y0, h, tf)
t, y_euler_mejorado = euler_mejorado(f, t0, y0, h, tf)

# Visualización
plt.figure(figsize=(10, 6))
plt.plot(t, y_euler, label="Método de Euler", marker='o')
plt.plot(t, y_euler_mejorado, label="Método de Euler Mejorado", marker='s')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Comparación de soluciones de EDO usando Euler y Euler Mejorado')
plt.legend()
plt.grid(True)
plt.show()

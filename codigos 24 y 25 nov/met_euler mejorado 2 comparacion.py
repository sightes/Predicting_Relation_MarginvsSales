# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función para el método de Euler
def euler(f, x0, y0, h, x_final):
    n = int((x_final - x0) / h)
    x = np.linspace(x0, x_final, n)
    y = np.zeros(n)
    y[0] = y0

    for i in range(1, n):
        y[i] = y[i - 1] + h * f(x[i - 1], y[i - 1])
    
    return x, y

# Definición de la función para el método de Euler mejorado (Heun)
def euler_mejorado(f, x0, y0, h, x_final):
    n = int((x_final - x0) / h)
    x = np.linspace(x0, x_final, n)
    y = np.zeros(n)
    y[0] = y0

    for i in range(1, n):
        pendiente_inicio = f(x[i - 1], y[i - 1])
        y_pred = y[i - 1] + h * pendiente_inicio
        pendiente_fin = f(x[i], y_pred)
        y[i] = y[i - 1] + h * (pendiente_inicio + pendiente_fin) / 2
    
    return x, y

# Ecuación diferencial y' = x^3 + y
f = lambda x, y: x**3 + y

# Condiciones iniciales y parámetros
x0 = 0
y0 = 1
h = 0.1  # Tamaño de paso
x_final = 2

# Aplicar el método de Euler
x, y_euler = euler(f, x0, y0, h, x_final)

# Aplicar el método de Euler mejorado
x, y_euler_mejorado = euler_mejorado(f, x0, y0, h, x_final)

# Visualización
plt.figure(figsize=(12, 6))
plt.plot(x, y_euler, label="Solución Euler", marker='o', color='blue')
plt.plot(x, y_euler_mejorado, label="Solución Euler Mejorado", marker='s', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Comparación de la Solución de Euler y Euler Mejorado")
plt.legend()
plt.grid(True)
plt.show()

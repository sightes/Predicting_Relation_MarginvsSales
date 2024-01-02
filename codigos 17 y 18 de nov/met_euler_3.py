#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
código para resolver la ecuación diferencial 
y' = y + x que se encuentra en las diapositivas
mediante el método de Euler

"""

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función para el método de Euler
# funcion int es para transformar numeros decimales a enteros 
def euler(f, x0, y0, h, x_final):
    n = int((x_final - x0) / h)
    x = np.linspace(x0, x_final, n)
    y = np.zeros(n)
    y[0] = y0

    for i in range(1, n):
        y[i] = y[i - 1] + h * f(x[i - 1], y[i - 1])
    
    return x, y

# Ecuación diferencial y' = x + y
f = lambda x, y: x + y

# Solución analítica
solucion_analitica = lambda x: -1 - x + 2 * np.exp(x)

# Condiciones iniciales y parámetros
x0, y0 = 0, 1
h = 0.1  # Tamaño de paso
x_final = 2

# Aplicar el método de Euler
x, y_euler = euler(f, x0, y0, h, x_final)

# Calcular la solución analítica
y_exacta = solucion_analitica(x)

# Visualización
plt.figure(figsize=(12, 6))
plt.plot(x, y_euler, label="Solución Euler", marker='o')
plt.plot(x, y_exacta, label="Solución Exacta", linestyle='dashed')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Comparación de la Solución de Euler con la Solución Analítica")
plt.legend()
plt.grid(True)
plt.show()

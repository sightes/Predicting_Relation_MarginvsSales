#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
código para resolver la ecuación diferencial 
y' = y + x que se encuentra en las diapositivas
mediante el método de Euler.
incluye gráfico del error de truncamiento.
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

# Calcular el error de truncamiento
error_truncamiento = np.abs(y_exacta - y_euler)

# Visualización
plt.figure(figsize=(12, 8))

# Gráfico de las soluciones
plt.subplot(2, 1, 1)
plt.plot(x, y_euler, label="Solución Euler", marker='o')
plt.plot(x, y_exacta, label="Solución Exacta", linestyle='dashed')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Comparación de la Solución de Euler con la Solución Analítica")
plt.legend()
plt.grid(True)

# Gráfico del error de truncamiento
plt.subplot(2, 1, 2)
plt.plot(x, error_truncamiento, label="Error de Truncamiento", color='red', marker='x')
plt.xlabel('x')
plt.ylabel('Error')
plt.title("Error de Truncamiento")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

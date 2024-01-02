#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 08:04:35 2023

@author: javierurrutia
"""

import numpy as np
import matplotlib.pyplot as plt

# Definición de parámetros y condiciones iniciales
t0 = 0       # Tiempo inicial
tf = 1       # Tiempo final
y0 = 1       # Condición inicial
h = 0.1      # Paso de tiempo

# Función de la ecuación diferencial y' = y
def f(y):
    return y

# Inicialización de variables
t = np.arange(t0, tf + h, h)
y_euler = np.zeros(len(t))
y_exact = np.zeros(len(t))
y_euler[0] = y0
y_exact[0] = y0

# Método de Euler
for i in range(len(t) - 1):
    y_euler[i + 1] = y_euler[i] + h * f(y_euler[i])
    y_exact[i + 1] = np.exp(t[i + 1])

# Cálculo del error de truncamiento
truncation_error = np.abs(y_exact - y_euler)

# Visualización
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, y_euler, 'b-o', label='Solución Euler')
plt.plot(t, y_exact, 'r-*', label='Solución Exacta')
plt.xlabel('Tiempo (t)')
plt.ylabel('y')
plt.title('Comparación entre Método de Euler y Solución Exacta')
plt.legend()
plt.grid(True)

# Visualización del error de truncamiento
plt.subplot(2, 1, 2)
plt.plot(t, truncation_error, 'k-x')
plt.xlabel('Tiempo (t)')
plt.ylabel('Error de Truncamiento')
plt.title('Error de Truncamiento en el Método de Euler')
plt.grid(True)
plt.tight_layout()
plt.show()

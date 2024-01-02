#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 07:55:09 2023

@author: javierurrutia
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
m = 1.0  # Masa
k = 50.0 # Constante del resorte
b = 0.5  # Coeficiente de amortiguamiento

# Función para el sistema de ecuaciones
def sistema(t, y):
    x, v = y
    dxdt = v
    dvdt = (-b * v - k * x) / m
    return np.array([dxdt, dvdt])

# Condiciones iniciales y parámetros de simulación
x0 = 1.0   # Posición inicial
v0 = 0.0   # Velocidad inicial
t0 = 0     # Tiempo inicial
tf = 10    # Tiempo final
h = 0.01   # Paso de tiempo

# Inicialización
t = np.arange(t0, tf, h)
n = len(t)
y = np.zeros((n, 2))
y[0] = [x0, v0]

# Método de Euler
for i in range(n - 1):
    y[i + 1] = y[i] + h * sistema(t[i], y[i])

# Visualización
plt.plot(t, y[:, 0], label='Posición (x)')
plt.plot(t, y[:, 1], label='Velocidad (v)')
plt.xlabel('Tiempo (t)')
plt.ylabel('Valores')
plt.title('Oscilador Armónico')
plt.legend()
plt.grid(True)
plt.show()

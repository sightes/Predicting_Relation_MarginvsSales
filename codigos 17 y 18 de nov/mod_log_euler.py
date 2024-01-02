#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codigo python para resolver el modelo logistico de crecimient
mediante el metodo de Euler.
Sigue los siguientes pasos:
1.- Define los parámetros del modelo logístico de crecimiento de población.
2.- Establece los parámetros de la simulación, incluyendo el tiempo total y
 el paso de tiempo.
3.- Inicializa un arreglo para almacenar los valores de la población en 
cada paso y otro para el tiempo.
4.- Implementa el método de Euler para calcular la población 
en cada paso de tiempo.
5.- Visualiza la población en función del tiempo con un gráfico.
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del Modelo Logístico
r = 0.1   # Tasa de crecimiento
K = 500   # Capacidad de carga
P0 = 50   # Población inicial

# Parámetros de la simulación
T = 50    # Tiempo total de simulación
dt = 0.5  # Paso de tiempo (h)
n = int(T / dt)  # Número de pasos

# Inicialización
P = np.zeros(n)  # Vector para almacenar la población en cada paso
t = np.arange(0, T, dt)  # Vector de tiempo
P[0] = P0  # Condición inicial

# Método de Euler
for i in range(n - 1):
    dP = r * P[i] * (1 - P[i] / K)  # Modelo logístico
    P[i + 1] = P[i] + dP * dt       # Método de Euler

# Visualización
plt.plot(t, P)
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Modelo Logístico de Crecimiento de Población')
plt.grid(True)
plt.show()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
código para resolver la ecuación diferencial de desintegracion
radiactiva dN/dt = -lambda * N
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de desintegración radiactiva
lambda_ = 0.01  # Constante de desintegración
N0 = 1000       # Cantidad inicial de sustancia

# Parámetros de simulación
T = 100   # Tiempo total de simulación
dt = 1    # Paso de tiempo
n = int(T / dt)

# Inicialización
N = np.zeros(n)
t = np.linspace(0, T, n)
N[0] = N0

# Método de Euler
for i in range(n - 1):
    N[i + 1] = N[i] - lambda_ * N[i] * dt

# Visualización
plt.plot(t, N)
plt.xlabel('Tiempo')
plt.ylabel('Cantidad de Sustancia')
plt.title('Modelo de Desintegración Radiactiva')
plt.grid(True)
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 16:57:52 2023

@author: jum00
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del péndulo
g = 9.81  # aceleración debida a la gravedad (m/s^2)
L = 1.0   # longitud del péndulo (m)
theta0 = np.pi / 4  # ángulo inicial (radianes)
omega0 = 0.0  # velocidad angular inicial (rad/s)

# Parámetros de la simulación
dt = 0.01  # tamaño del paso (s)
T = 10     # tiempo total de simulación (s)
n = int(T / dt)

# Inicialización
theta = np.zeros(n)
omega = np.zeros(n)
t = np.linspace(0, T, n)
theta[0] = theta0
omega[0] = omega0
error_truncamiento = np.zeros(n)

# Método de Euler y estimación del error de truncamiento
for i in range(n - 1):
    dtheta = omega[i]
    domega = -g / L * np.sin(theta[i])
    theta[i + 1] = theta[i] + dtheta * dt
    omega[i + 1] = omega[i] + domega * dt
    # Estimación del error (aproximación)
    error_truncamiento[i + 1] = (dt**2 / 2) * abs(-g / L * np.cos(theta[i]) * omega[i])

# Gráfico
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, theta)
plt.ylabel('Ángulo (rad)')
plt.title('Péndulo Simple: Ángulo y Error de Truncamiento')

plt.subplot(2, 1, 2)
plt.plot(t, error_truncamiento)
plt.xlabel('Tiempo (s)')
plt.ylabel('Error de Truncamiento')
plt.show()

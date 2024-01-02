#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 07:29:16 2023

@author: javierurrutia
"""

import numpy as np
import matplotlib.pyplot as plt

# Definición de parámetros y condiciones iniciales
m = 1  # Masa
t0 = 0  # Tiempo inicial
tf = 10  # Tiempo final
x0 = 0  # Condición inicial para x
v0 = 1  # Condición inicial para v (x')
h = 0.01  # Paso de tiempo

# Definición de la función F(t, x, v)
def F(t, x, v):
    return -9.81 * m  # Fuerza gravitacional

# Inicialización de variables
t = np.arange(t0, tf + h, h)  # Crear arreglo de tiempo
x = np.zeros(len(t))  # Inicializar arreglo de posición
v = np.zeros(len(t))  # Inicializar arreglo de velocidad
x[0] = x0
v[0] = v0

# Método de Euler para resolver el sistema de ecuaciones
for i in range(len(t)-1):
    v[i+1] = v[i] + h * F(t[i], x[i], v[i]) / m
    x[i+1] = x[i] + h * v[i]

# Visualización
plt.plot(t, x)
plt.xlabel('Tiempo (t)')
plt.ylabel('Posición (x)')
plt.title('Solución de la Segunda Ley de Newton usando el Método de Euler')
plt.grid(True)
plt.show()

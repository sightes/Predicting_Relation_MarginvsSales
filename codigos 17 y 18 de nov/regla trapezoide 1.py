# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:26:33 2023

@author: jum00
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir la función a integrar
def f(x):
    return x**2

# Intervalo de integración
a = 0  # Límite inferior
b = 1  # Límite superior
n = 70 # Número de puntos en la malla

# Crear una malla de puntos
x = np.linspace(a, b, n)
y = f(x)

# Aplicar la regla del trapecio
integral = np.trapz(y, x)

# Visualización
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f'f(x) = x^2', color='blue')

# Rellenar el área bajo la curva
plt.fill_between(x, y, color='skyblue', alpha=0.4)

# Detalles del gráfico
plt.title(f'Integral de f(x) = x^2 en el intervalo [{a}, {b}]')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

print(f'El valor aproximado de la integral es: {integral}')

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 16:20:28 2023

@author: jum00
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros
k = 0.1  # constante de proporcionalidad
T_ambiente = 20  # Temperatura ambiente
T0 = 100  # Temperatura inicial del objeto
dt = 0.1  # Tamaño del paso
tiempo_total = 50  # Tiempo total de simulación

# Inicialización
n = int(tiempo_total / dt)
T = np.zeros(n)
t = np.linspace(0, tiempo_total, n)
T[0] = T0

# Método de Euler
for i in range(n - 1):
    dT = -k * (T[i] - T_ambiente)
    T[i + 1] = T[i] + dT * dt

# Cálculo del error de truncamiento acumulado
error_truncamiento_acumulado = n * k * dt**2

# Gráfico
plt.figure(figsize=(12, 6))
plt.plot(t, T, label='Temperatura (Método de Euler)')
plt.axhline(y=error_truncamiento_acumulado, color='r', linestyle='--', label=f'Error de Truncamiento Acumulado: {error_truncamiento_acumulado:.2e}')
plt.xlabel('Tiempo')
plt.ylabel('Temperatura / Error')
plt.title("Ley de Enfriamiento de Newton y Error de Truncamiento Acumulado\nEn este caso el error de truncamiento es 0 porque la ecuación el lineal")
plt.legend()
plt.grid(True)
plt.show()



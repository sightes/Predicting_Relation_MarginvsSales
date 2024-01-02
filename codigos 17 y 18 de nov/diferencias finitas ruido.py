# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:41:42 2023

@author: jum00
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Generar datos ruidosos
t = np.linspace(0, 10, 100)
f = np.sin(t) + np.random.normal(0, 0.1, t.shape)  # Función seno con ruido

# Aplicar filtro de Savitzky-Golay para suavizar los datos
f_smooth = savgol_filter(f, window_length=11, polyorder=3)

# Calcular la derivada numérica
dfdt = np.gradient(f_smooth, t)

# Visualización
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, f, label='Datos Ruidosos')
plt.plot(t, f_smooth, label='Datos Suavizados')
plt.legend()
plt.title('Función Original y Suavizada')

plt.subplot(2, 1, 2)
plt.plot(t, dfdt, label='Derivada Numérica')
plt.legend()
plt.title('Derivada Numérica de la Función Suavizada')
plt.xlabel('Tiempo (t)')
plt.show()

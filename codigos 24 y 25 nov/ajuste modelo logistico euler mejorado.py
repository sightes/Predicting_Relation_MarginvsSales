# -*- coding: utf-8 -*-
"""
Ejercicio de ajuste de los parámetros de la ecuación diferencial 
a un set de datos observados del modelo logístico mediante euler mejorado
valores reales:
    r = 0.1
    k = 100
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Función para el modelo logístico
def modelo_logistico(P, r, K):
    return r * P * (1 - P / K)

# leemos el archivo excel con la librería pandas
datos = pd.read_excel('datos.xlsx')

# Asumiendo que el archivo tiene columnas 'tiempo' y 'poblacion'
tiempo = datos['tiempo'].to_numpy()
poblacion_observada = datos['poblacion'].to_numpy()

# Parámetros del Modelo Logístico (ajustar según sea necesario)
r = 0.3   # Tasa de crecimiento
K = 1000   # Capacidad de carga
P0 = poblacion_observada[0]  # Población inicial basada en los datos

# Parámetros de la simulación
T = tiempo[-1]  # Tiempo total de simulación basado en los datos
dt = 0.1  # Paso de tiempo (ajustar según sea necesario)
n = int(T / dt)  # Número de pasos

# Inicialización para el Modelo Logístico
P = np.zeros(n)  # Vector para almacenar la población en cada paso
t_modelo = np.arange(0, T, dt)  # Vector de tiempo para el modelo
P[0] = P0  # Condición inicial

# Método de Euler Mejorado (Método de Heun) para el Modelo Logístico
for i in range(n - 1):
    dP_inicio = modelo_logistico(P[i], r, K)
    P_pred = P[i] + dP_inicio * dt
    dP_fin = modelo_logistico(P_pred, r, K)
    P[i + 1] = P[i] + (dP_inicio + dP_fin) * dt / 2  # Promedio de pendientes

# Visualización de los datos observados y el modelo
plt.figure(figsize=(10, 6))
plt.plot(tiempo, poblacion_observada, 'o', label='Población Observada')
plt.plot(t_modelo, P, label='Modelo Logístico Mejorado')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Comparación de Población Observada y Modelo Logístico Mejorado')
plt.legend()
plt.grid(True)
plt.show()

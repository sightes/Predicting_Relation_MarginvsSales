# -*- coding: utf-8 -*-
"""
código para estimar r y K del modelo logístico usando metodologías de optimización
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Función para el modelo logístico
def modelo_logistico(t, P0, r, K):
    return K / (1 + ((K - P0) / P0) * np.exp(-r * t))

# leemos el archivo excel con la librería pandas
datos = pd.read_excel('datos.xlsx')

# Asumiendo que el archivo tiene columnas 'tiempo' y 'poblacion'
tiempo = datos['tiempo'].to_numpy()
poblacion_observada = datos['poblacion'].to_numpy()

# Estimación inicial de los parámetros
P0 = poblacion_observada[0]  # Población inicial basada en los datos
estimacion_inicial = [P0, 0.3, 1000]  # [P0, r, K]

# Ajuste del modelo logístico a los datos
parametros_optimizados, covarianza = curve_fit(modelo_logistico, tiempo, poblacion_observada, p0=estimacion_inicial)

# Parámetros optimizados y sus errores estándar
P0_opt, r_opt, K_opt = parametros_optimizados
error_estandar = np.sqrt(np.diag(covarianza))

# Imprimir los resultados
print(f"Parámetros optimizados: P0 = {P0_opt:.2f}, r = {r_opt:.4f}, K = {K_opt:.2f}")
print(f"Errores estándar: P0 = {error_estandar[0]:.2f}, r = {error_estandar[1]:.4f}, K = {error_estandar[2]:.2f}")

# Usar los parámetros optimizados para predecir la población
poblacion_predicha = modelo_logistico(tiempo, P0_opt, r_opt, K_opt)

# Visualización de los datos observados y el modelo
plt.figure(figsize=(10, 6))
plt.plot(tiempo, poblacion_observada, 'o', label='Población Observada')
plt.plot(tiempo, poblacion_predicha, label='Modelo Logístico Ajustado')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Comparación de Población Observada y Modelo Logístico Ajustado')
plt.legend()
plt.grid(True)
plt.show()

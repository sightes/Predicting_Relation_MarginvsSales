#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 08:06:58 2023

@author: javierurrutia
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import pandas as pd

# Cargar los datos del dólar diario
df = pd.read_excel("economico.xlsx")

# Seleccionar la columna del precio del dólar
k_obs = df["capital"].to_numpy()

# Seleccionar la columna de la fecha
t_obs = df['Tiempo'].to_numpy()

# Función del modelo
def solow_model(t, k, s, alpha, n, d):
    return s * k**alpha - (n + d) * k

# Condiciones iniciales
k0 = 0.5     # Capital inicial per cápita
t_span = (0, 100)  # Intervalo de tiempo
n_1 = 1000
t_eval = np.linspace(t_span[0], t_span[1], n_1)


# Función para calcular la solución del modelo
def model_solution(params):
    s, alpha, n, d = params
    sol = solve_ivp(solow_model, t_span, [k0], args=(s, alpha, n, d), method='RK45', t_eval=t_obs)
    return sol.y[0]

# Función de costo
def cost_function(params):
    k_model = model_solution(params)
    return np.mean((k_model - k_obs)**2)

# Parámetros iniciales para la optimización
initial_params = [0.1, 0.1, 0.01, 0.05]

# Optimización
result = minimize(cost_function, initial_params, method='Nelder-Mead')

# Parámetros optimizados
optimized_params = result.x

# Resolución de la ecuación diferencial con parámetros optimizados
sol_optimized = solve_ivp(solow_model, t_span, [k0], args=tuple(optimized_params), method='RK45', t_eval=t_eval)
print(optimized_params)

# Gráfico de la solución y los datos observados
plt.plot(sol_optimized.t, sol_optimized.y[0], label='Modelo Optimizado')
plt.scatter(t_obs, k_obs, color='red', label='Datos Observados')
plt.title('Modelo de Crecimiento de Solow-Swan con Parámetros Optimizados')
plt.xlabel('Tiempo')
plt.ylabel('Capital per cápita')
plt.legend()
plt.grid(True)
plt.show()

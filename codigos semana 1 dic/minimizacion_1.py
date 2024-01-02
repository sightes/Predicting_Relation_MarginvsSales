# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import pandas as pd

# Función de la ecuación diferencial
def funcion(t, k, s, alpha, n, d):
    return s * k**alpha - (n + d) * k

# Función para calcular la solución de la ecuación diferencial con parámetros dados
def solve_equation(params):
    s, alpha, n, d = params
    resultado = solve_ivp(funcion, (0, 100), [0.5], args=(s, alpha, n, d), t_eval=t_eval)
    return resultado.y[0]

# Función objetivo para la optimización (ajuste de curvas)
def objective(params):
    model_solution = solve_equation(params)
    return np.sum((model_solution - valores_obs)**2)  # Minimizar la suma de cuadrados de las diferencias

# Datos observados (ejemplo, reemplazar con tus datos)
observed_data = pd.read_excel("economico.xlsx")
valores_obs = observed_data["capital"].to_numpy()
tiempo = observed_data["Tiempo"].to_numpy()
t_min = tiempo[0]
t_max = tiempo[-1]
t_eval = np.linspace(t_min, t_max, 1000)

# Valores iniciales para los parámetros
initial_guess = [0.3, 0.3, 0.01, 0.05]

# Optimización
result = minimize(objective, initial_guess, method='BFGS')
optimized_params = result.x

# Usar los parámetros optimizados para resolver la ecuación diferencial
optimized_solution = solve_ivp(funcion, (0, 100), [0.5], args=tuple(optimized_params), t_eval=t_eval)

# Graficar la solución optimizada
plt.plot(optimized_solution.t, optimized_solution.y[0])
plt.title('Modelo de Crecimiento de Solow-Swan con Parámetros Optimizados')
plt.xlabel('Tiempo')
plt.ylabel('Capital per cápita')
plt.grid(True)
plt.show()

# Guardar los resultados
resultados = pd.DataFrame({
    'Tiempo': optimized_solution.t,
    'capital': optimized_solution.y[0]
})
nombre_archivo = 'resultados_optimizados.xlsx'
resultados.to_excel(nombre_archivo, index=False)

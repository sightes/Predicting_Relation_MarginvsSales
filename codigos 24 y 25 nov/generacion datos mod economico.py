#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import pandas as pd

# Definición de la función que representa la ecuación diferencial del modelo de Solow-Swan
def solow_model(t, k, s, alpha, n, d):
    return s * k**alpha - (n + d) * k

# Parámetros del modelo
s = 0.3      # Tasa de ahorro
alpha = 0.3  # Elasticidad de la producción
n = 0.01     # Tasa de crecimiento de la población
d = 0.05     # Tasa de depreciación del capital

# Condiciones iniciales
k0 = 0.5     # Capital inicial per cápita
t_span = (0, 100)  # Intervalo de tiempo
n_1 = 1000
t_eval = np.linspace(t_span[0], t_span[1], n_1)

# Resolución de la ecuación diferencial
sol = solve_ivp(solow_model, t_span, [k0], args=(s, alpha, n, d), method='RK45', t_eval=t_eval)

# Crear un DataFrame de Pandas con los resultados
resultados = pd.DataFrame({
    'Tiempo': sol.t,
    'capital': sol.y[0]
})

# Guardar el DataFrame en un archivo Excel
nombre_archivo = 'economico.xlsx'
resultados.to_excel(nombre_archivo, index=False)
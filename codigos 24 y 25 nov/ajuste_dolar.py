#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# Suponiendo que data_clean ya está definido y contiene las columnas 'Dia' y 'Valor'

# Definir una función para el ajuste polinomial
def funcion(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# Cargar los datos del dólar diario
df = pd.read_excel("Indicador.xls")

# Seleccionar la columna del precio del dólar
y = df["Valor"].to_numpy()

# Seleccionar la columna de la fecha
x = df['time'].to_numpy()

# Intentar un ajuste polinomial con una estimación inicial
resultados = curve_fit(funcion, x, y, p0=[1, 1, 1, 1])

# Parámetros estimados
a, b, c, d = resultados[0]

# imprime los parámetros estimados
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)


# # Graficar los datos
plt.plot(x, y, "o")

# # Graficar la función ajustada
x_new = np.linspace(x.min(), x.max(), 100)
y_new = funcion(x_new, a, b, c, d)
plt.plot(x_new, y_new)

# # Título y etiquetas del eje
plt.title("Dolar diario")
plt.xlabel("Fecha")
plt.ylabel("Precio (USD)")

# # Mostrar la gráfica
plt.show()

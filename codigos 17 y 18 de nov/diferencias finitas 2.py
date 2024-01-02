# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:28:03 2023

@author: jum00
"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")


# definir los tamaños de los pasos
h = 1
# definir el numero de iteraciones a desarrollar
iterations = 20
# lista para almacenar los tamaños de los pasos
step_size = []
# lista para almacenar el error máximo por cada tamaño de paso
max_error = []

for i in range(iterations):
    # divide el tamaño de paso
    h /= 2
    # almacena cada tamaño de paso
    step_size.append(h)
    # calcula la nueva grilla
    x = np.arange(0, 2 * np.pi, h)
    # calcular el valor de la función en la malla
    y = np.cos(x)
    # calcular el vector de diferencias hacia delante
    forward_diff = np.diff(y)/h
    # calcular la malla correspondiente
    x_diff = x[:-1]
    # calcula la solución exacta
    exact_solution = -np.sin(x_diff)
    # calcula el error máximo entre la derivada numérica
    # y la solución exacta
    max_error.append(max(abs(exact_solution - forward_diff)))
    
# producir un gráfico logarítmico del error máximo en función 
# del tamaño del paso
plt.figure(figsize = (12, 8))
plt.loglog(step_size, max_error, "v")
plt.xlabel("Tamaño de paso")
plt.ylabel("Error máximo")
plt.show()


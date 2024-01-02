# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")
#%matplotlib inline

# definir los saltos
h = 0.1
# denifir la malla
x = np.arange(0, 2*np.pi, h)
# calcular la funcion
y = np.cos(x)

# calcular el vector de diferencias hacia adelante
forward_diff = np.diff(y)/h
# calcular la malla correspondiente
x_diff = x[:-1:]
# calcular la solución exacta
exact_solution = -np.sin(x_diff)

# graficar la solucion
plt.figure(figsize = (12, 8))
plt.plot(x_diff, forward_diff, "-", \
label = "aproximacion de diferencias finitas")
plt.plot(x_diff, exact_solution, label = "solucion exacta")
plt.legend()
plt.show()

# calcular el error entre la derivada numérica y la solucion exacta
max_error = max(abs(exact_solution - forward_diff))
print(max_error)
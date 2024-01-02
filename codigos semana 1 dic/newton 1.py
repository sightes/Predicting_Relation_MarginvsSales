# -*- coding: utf-8 -*-
"""

"""

import scipy.optimize as opt
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 4  # Función cuya raíz queremos encontrar

def df(x):
    return 2*x  # Derivada de f(x)

def newton_method(f, df, x0, tol=1e-10, max_iter=1000):
    x = x0
    iteraciones = [x]  # Lista para almacenar las iteraciones
    for _ in range(max_iter):
        x_new = x - f(x) / df(x)
        iteraciones.append(x_new)
        if abs(x_new - x) < tol:  # Condición de parada
            break
        x = x_new
    return x, iteraciones

x0 = 1.0  # Valor inicial
root, iteraciones = newton_method(f, df, x0)

# Imprimir la raíz encontrada
print("La raíz es:", root)

# Graficar las iteraciones
plt.plot(iteraciones, label='x en cada iteración')
plt.xlabel('Iteración')
plt.ylabel('x')
plt.title('Iteraciones del Método de Newton-Raphson')
plt.legend()
plt.show()



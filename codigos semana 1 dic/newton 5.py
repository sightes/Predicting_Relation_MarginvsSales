# -*- coding: utf-8 -*-
"""
graficar en desmos la funcion
se utiliza como argumento la derivada porque la funcion opt.newton
debe tener una funcion  x
probar la funcion original cambiando el número de iteraciones
"""

import scipy.optimize as opt

def f(x):
    return (x - 2)**2 + 3  # Función (x - 2)^2 + 3

def df(x):
    return 2*(x - 2)  # Derivada

x0 = 1.0  # Valor inicial

# Usando scipy.optimize.newton para encontrar donde la derivada es cero
extremo = opt.newton(df, x0)

# Verificar si es un mínimo usando la segunda derivada
def ddf(x):
    return 2  # Segunda derivada

if ddf(extremo) > 0:
    print("El mínimo encontrado es en x =", extremo)
else:
    print("El punto encontrado en x =", extremo, "no es un mínimo")

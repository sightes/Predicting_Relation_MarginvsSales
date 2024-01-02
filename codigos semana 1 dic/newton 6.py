# -*- coding: utf-8 -*-
"""
método de newton
probar distintos valores iniciales y probar
probar si mejora la solucion colocando la derivada
"""

import scipy.optimize as opt

def f(x):
    return x**2 - 5*x + 6  # Polinomio x^2 - 5x + 6

def df(x):
    return 2*x - 5  # Derivada del polinomio

x0 = 100  # Valor inicial

# root = opt.newton(f, x0, fprime=df)
root = opt.newton(f, x0)
print("La raíz encontrada es:", root)

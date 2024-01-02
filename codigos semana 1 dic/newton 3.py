# -*- coding: utf-8 -*-
"""
metodo de Newton Raphson para polinomios
probar con valor inicial de 1.5 y -1.5
graficar en desmos
El resultado que se obtenga de la función dependerá del
valor inicial
"""

import scipy.optimize as opt

def f(x):
    return x**3 - 2*x**2 - 4*x + 8  # Polinomio x^3 - 2x^2 - 4x + 8

def df(x):
    return 3*x**2 - 4*x - 4  # Derivada del polinomio

x0 = 1.5  # Valor inicial

# Usando scipy.optimize.newton
root = opt.newton(f, x0, fprime=df)
print("La raíz encontrada es:", root)


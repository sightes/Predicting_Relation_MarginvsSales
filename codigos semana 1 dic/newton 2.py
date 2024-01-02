# -*- coding: utf-8 -*-
"""

"""

import scipy.optimize as opt

def f(x):
    return x**2 - 4  # Ejemplo: función cuya raíz queremos encontrar

def df(x):
    return 2*x  # Derivada de f(x)

x0 = 1.0  # Valor inicial

root = opt.newton(f, x0, fprime=df)  # Uso de scipy.optimize.newton
print("La raíz es:", root)
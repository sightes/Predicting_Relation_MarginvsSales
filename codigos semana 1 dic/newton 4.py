# -*- coding: utf-8 -*-
"""
Graficar en desmos
probar distintos valores iniciales
"""

import numpy as np
import scipy.optimize as opt

def f(x):
    return x * np.sin(x) - np.cos(x)  # Ecuación trascendental x*sin(x) - cos(x)

def df(x):
    return np.sin(x) + x * np.cos(x) + np.sin(x)  # Derivada de la ecuación

x0 = 0.5  # Valor inicial

# Usando scipy.optimize.newton
root = opt.newton(f, x0, fprime=df)
print("La raíz encontrada es:", root)

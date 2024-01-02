# -*- coding: utf-8 -*-
"""

"""
from scipy.optimize import fsolve

def sistema(x):
    return [x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2 - 1, 
            x[0] + x[1]**2 - x[2] + x[3]**3 - 2, 
            x[0]**2 - x[1] + x[2]**2 - x[3] - 1, 
            x[0] - x[1]**2 + x[2] - x[3]**2 + 1]

solucion = fsolve(sistema, [1, 1, 1, 1])
print("Solución del sistema 4:", solucion)
# -*- coding: utf-8 -*-
"""
resolucion sistemas no lineales
"""

import numpy as np
from scipy.optimize import fsolve

def sistema_ecuaciones(x):
    # x[0] = cantidad de producto 1, x[1] = cantidad de producto 2
    # Ejemplo hipotético de ecuaciones de oferta y demanda
    ec1 = x[0]**2 - x[1] - 10  # Ecuación 1
    ec2 = x[1] + 3*x[0]*x[1]**2 - 57  # Ecuación 2
    return [ec1, ec2]

solucion_inicial = [1, 1]  # Estimación inicial

solucion = fsolve(sistema_ecuaciones, solucion_inicial)
print(f"Solución del sistema: {solucion}")

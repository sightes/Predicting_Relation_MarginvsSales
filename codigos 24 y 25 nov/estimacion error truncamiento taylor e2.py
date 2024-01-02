# -*- coding: utf-8 -*-
"""
Codigo para estimar el error de truncamiento de la serie de 
Taylor para estimar el valor de e2
"""

import numpy as np
import matplotlib.pyplot as plt

# se inicializa el valor de e en 0 para que vaya actualizándose
exp = 0
x = 2
true_value = np.exp(2)
errors = []

# implementacion de la serie de Taylor
for i in range(10):
    exp = exp + (x**i)/np.math.factorial(i)
    error = abs(true_value - exp)
    errors.append(error)
    print(f"Using {i}-term, {exp}")
    print(f"The true e^2 is: \n{np.exp(2)}")
    print(f"Error: {error}\n")
    
# Graficar el error de truncamiento
plt.plot(range(10), errors, marker='o')
plt.title("Error de Truncamiento en la Serie de Taylor para e^2")
plt.xlabel("Número de Términos")
plt.ylabel("Error de Truncamiento")
plt.yscale('log')  # Escala logarítmica para una mejor visualización
plt.grid(True)
plt.show()
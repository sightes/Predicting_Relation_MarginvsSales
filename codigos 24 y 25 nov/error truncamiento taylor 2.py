# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import matplotlib.pyplot as plt

def taylor_cos(x, N):
    sum = 0
    for n in range(N):
        sum += ((-1)**n) * (x**(2*n)) / np.math.factorial(2*n)
    return sum

x = np.pi / 4  # Un punto específico para evaluar
true_value = np.cos(x)
terms = range(1, 11)  # Número de términos en la serie
errors = []

for N in terms:
    approx_value = taylor_cos(x, N)
    error = np.abs(true_value - approx_value)
    errors.append(error)

plt.plot(terms, errors, 'o-')
plt.title(r'Error de Truncamiento en la Serie de Taylor para $\cos(\frac{\pi}{4})$')
plt.xlabel('Número de Términos')
plt.ylabel('Error Absoluto')
plt.yscale('log')
plt.grid(True)
plt.show()


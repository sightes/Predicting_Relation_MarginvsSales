# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import matplotlib.pyplot as plt

def taylor_ln1p(x, N):
    sum = 0
    for n in range(1, N):
        sum += ((-1)**(n+1)) * (x**n) / n
    return sum

x = 0.5  # Un punto específico para evaluar
true_value = np.log1p(x)
terms = range(1, 11)  # Número de términos en la serie
errors = []

for N in terms:
    approx_value = taylor_ln1p(x, N)
    error = np.abs(true_value - approx_value)
    errors.append(error)

plt.plot(terms, errors, 'o-')
plt.title(r'Error de Truncamiento en la Serie de Taylor para $\ln(1 + 0.5)$')
plt.xlabel('Número de Términos')
plt.ylabel('Error Absoluto')
plt.yscale('log')
plt.grid(True)
plt.show()



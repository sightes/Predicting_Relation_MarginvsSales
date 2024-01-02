# -*- coding: utf-8 -*-
"""
primer ejemplo de serie de taylor
"""

import numpy as np
import matplotlib.pyplot as plt

# inicializar las variables
x = np.linspace(-np.pi, np.pi, 200)
y = np.zeros(len(x))

# colocar etiquetas para los distintos órdenes de la serie de taylor
labels = ["First Order", "Third Order",
"Fifth Order", "Seventh Order"]

# configuracion de la figura
plt.figure(figsize = (10,8))

#implementación de la serie de taylor
for n, label in zip(range(4), labels):
    y=y+((-1)**n*(x)**(2*n+1))/np.math.factorial(2*n+1)
    plt.plot(x,y, label = label)

# gráfico
plt.plot(x, np.sin(x), "k", label = "Analytic")
plt.grid()

# 1.- r antes de las comillas indica que la cadena es una cadena "raw" en 
# Python, lo que significa que los caracteres de escape (como \n) se tratan 
# literalmente y no necesitan ser escapados.
# 2.- $...$ es la forma de incluir expresiones matemáticas en formato LaTeX.
# 3.- \sum_{n=0}^{\infty} representa la suma desde n igual a 0 hasta el infinito.
# 4.- \frac{{(-1)}^n x^{2n+1}}{(2n+1)!} es la fracción que representa cada 
# término de la serie.
plt.title(r"Taylor Series Approximations of Various Orders\n"
          r"$y + \sum_{n=0}^{\infty} \frac{{(-1)}^n x^{2n+1}}{(2n+1)!}$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()



# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:46:27 2023

@author: jum00
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")

x = np.arange(0, 2*np.pi, 0.01)

# calcula la función 
omega = 100
epsilon = 0.01
y = np.cos(x)
y_noise = y + epsilon*np.sin(omega*x)

# grafica la solucion
plt.figure(figsize = (12, 8))
plt.plot(x, y_noise, "r-", label = "cos(x) + noise")
plt.plot(x, y, "b-", label = "cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
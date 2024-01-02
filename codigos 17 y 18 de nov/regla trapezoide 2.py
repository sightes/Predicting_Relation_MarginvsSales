# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:35:41 2023

@author: jum00
"""

import numpy as np

a = 0
b = np.pi
n = 11

# h is calculated as the difference between the upper and lower bounds
#  of the integration interval (b and a, respectively) divided by the number 
#  of subintervals (n minus 1).

h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sin(x)
I_trap = (h/2)*(f[0] + 2 * sum(f[1:n-1]) + f[n-1])
err_trap = 2 - I_trap

print(I_trap)
print(err_trap)
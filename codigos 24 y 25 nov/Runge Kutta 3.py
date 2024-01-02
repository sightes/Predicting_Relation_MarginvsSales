# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import matplotlib.pyplot as plt

def lotka_volterra(t, y, alpha=1.0, beta=0.1, delta=0.1, gamma=1.0):
    return np.array([alpha * y[0] - beta * y[0] * y[1], delta * y[0] * y[1] - gamma * y[1]])

def runge_kutta(f, t0, y0, h, tf):
    t = np.arange(t0, tf, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0

    for i in range(1, len(t)):
        k1 = h * f(t[i - 1], y[i - 1])
        k2 = h * f(t[i - 1] + h/2, y[i - 1] + k1/2)
        k3 = h * f(t[i - 1] + h/2, y[i - 1] + k2/2)
        k4 = h * f(t[i - 1] + h, y[i - 1] + k3)
        y[i] = y[i - 1] + (k1 + 2*k2 + 2*k3 + k4) / 6

    return t, y

t0, tf, h = 0, 30, 0.01
y0 = [10, 5]

t, y = runge_kutta(lotka_volterra, t0, y0, h, tf)

plt.plot(t, y[:, 0], label='Presa')
plt.plot(t, y[:, 1], label='Depredador')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title(r'Modelo Lotka-Volterra: $\frac{dx}{dt} = \alpha x - \beta xy, \frac{dy}{dt} = \delta xy - \gamma y$')
plt.legend()
plt.grid(True)
plt.show()
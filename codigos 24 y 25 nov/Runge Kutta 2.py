# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import matplotlib.pyplot as plt

def van_der_pol(t, y, mu=1.0):
    return np.array([y[1], mu * (1 - y[0]**2) * y[1] - y[0]])

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

# Parámetros iniciales
t0, tf, h = 0, 20, 0.01
y0 = [2, 0]

t, y = runge_kutta(van_der_pol, t0, y0, h, tf)

plt.plot(t, y[:, 0])
plt.xlabel('Tiempo')
plt.ylabel('Desplazamiento')
plt.title(r'Ecuación de Van der Pol: $\frac{d^2y}{dt^2} - \mu (1 - y^2) \frac{dy}{dt} + y = 0$')
plt.grid(True)
plt.show()

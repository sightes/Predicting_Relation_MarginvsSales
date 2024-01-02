# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import matplotlib.pyplot as plt


def pendulo_simple(t, y, g=9.81, l=1.0):
    return np.array([y[1], -g/l * np.sin(y[0])])

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

t0, tf, h = 0, 10, 0.01
y0 = [np.pi / 4, 0]  # Ángulo inicial de 45 grados y velocidad inicial 0

t, y = runge_kutta(pendulo_simple, t0, y0, h, tf)

plt.plot(t, y[:, 0])
plt.xlabel('Tiempo')
plt.ylabel('Ángulo (rad)')
plt.title(r'Péndulo Simple: $\frac{d^2\theta}{dt^2} + \frac{g}{l} \sin(\theta) = 0$')
plt.grid(True)
plt.show()

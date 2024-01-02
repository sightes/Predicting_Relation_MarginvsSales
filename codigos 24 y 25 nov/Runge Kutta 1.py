# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import matplotlib.pyplot as plt

# discretización de los pasos de tiempo
dt = 0.01

# rango del tiempo de simulación
time = np.arange(1.0, 4.0 + dt, dt)

# condiciones iniciales del sistema de segundo orden [y1, y2] @ t = 1
y0 = np.array([0, 1])  # y1 = 0, y2 = 1


def ode_system(_t, _y):
    """
    sistema de ecuaciones diferenciales de primer orden
    _t: valor del paso de tiempo discreto
    _y: vector de estado [y1, y2]
    """
    return np.array([_y[1], -_t * _y[1] + (2 / _t) * _y[0]])

# integración numérica de cuarto orden runge-kutta
def rk4(func, tk, _yk, _dt=0.01, **kwargs):
    """
    método de integración numérica de cuarto orden en un solo paso (RK4)
    func: sistema de EDO de primer orden
    tk: paso temporal actual
    _yk: vector de estado actual [y1, y2, y3, ...]
    _dt: tamaño del paso temporal discreto
    **kwargs: parámetros adicionales para el sistema ODE
    regresa: y evaluado en el tiempo k+1
    """

    # evaluar la derivada en varias etapas dentro del intervalo de tiempo
    f1 = func(tk, _yk, **kwargs)
    f2 = func(tk + _dt / 2, _yk + (f1 * (_dt / 2)), **kwargs)
    f3 = func(tk + _dt / 2, _yk + (f2 * (_dt / 2)), **kwargs)
    f4 = func(tk + _dt, _yk + (f3 * _dt), **kwargs)

    # devuelve una media de la derivada sobre tk, tk + dt
    return _yk + (_dt / 6) * (f1 + (2 * f2) + (2 * f3) + f4)

# ==============================================================
# propagar el estado

# resultados de la simulación
state_history = []

# inicializar yk
yk = y0

# inicializar tiempo
t = 0

# aproximar y en el tiempo t
for t in time:
    state_history.append(yk)
    yk = rk4(ode_system, t, yk, dt)

# convertir lista en matriz numpy
state_history = np.array(state_history)

print(f'y evaluado en el tiempo t = {t} segundos: {yk[0]}')

# Extraer y1 y y2 de state_history
y1_values = state_history[:, 0]
y2_values = state_history[:, 1]

# Crear la gráfica
plt.figure(figsize=(12, 6))

# Graficar y1 en función del tiempo
# y1 es la variable original. La designación de las variables y1 e y2 son 
# para reducir el orden de las derivadas parciales y aplicar el método.
# y2 corresponde a la derivada de y1, como lo establecido en las ecuaciones
# 3 y 4 del material.
plt.plot(time, y1_values, label='y1(t)', color='blue')

# Graficar y2 en función del tiempo
plt.plot(time, y2_values, label='y2(t)', color='red')

# Añadir título y etiquetas
plt.title('Historial de las Variables de Estado [y1, y2]')
plt.xlabel('Tiempo (t)')
plt.ylabel('Valores de Estado')
plt.grid(True)

# Añadir leyenda
plt.legend()

# Mostrar la gráfica
plt.show()
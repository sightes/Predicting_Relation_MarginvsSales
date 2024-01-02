#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# # "`solve_ivp` es una función de la biblioteca `scipy.integrate` en Python, utilizada 
# para resolver ecuaciones diferenciales ordinarias (EDOs). El nombre `solve_ivp` se refiere 
# a "solve initial value problem" (resolver problema de valor inicial), lo que significa que 
# está diseñada para resolver EDOs dadas ciertas condiciones iniciales.


# # Aquí hay algunos detalles clave sobre `solve_ivp`:

# # 1. **Problema de Valor Inicial**: `solve_ivp` resuelve EDOs del tipo 
# \( \frac{dy}{dt} = f(t, y) \), donde \( y \) puede ser un vector, es decir, 
# puede resolver sistemas de EDOs. Se requiere especificar el estado inicial d
# e \( y \) en el tiempo inicial \( t_0 \).

# # 2. **Argumentos**:
# #    - `fun`: La función que define la EDO, \( f(t, y) \).
# #    - `t_span`: Una tupla que define el intervalo de tiempo para la integración, \( (t_{\text{inicio}}, t_{\text{final}}) \).
# #    - `y0`: El estado inicial de \( y \) en \( t_{\text{inicio}} \).
# #    - `method`: El método numérico para la integración. Por ejemplo, 'RK45' es un método de Runge-Kutta de orden 4-5.
# #    - `args`: Argumentos adicionales para pasar a la función `fun`.
# #    - `t_eval`: Puntos de tiempo específicos en los que se desea obtener la solución.

# # 3. **Métodos de Integración**: `solve_ivp` incluye varios métodos de integración, c
# omo 'RK45' (Runge-Kutta de orden 4-5), 'RK23' (Runge-Kutta de orden 2-3), 
# 'DOP853' (un método de Runge-Kutta de orden 8), entre otros. Estos métodos 
# son adecuados para diferentes tipos de EDOs y tienen diferentes características en términos de precisión y eficiencia.

# # 4. **Resultado**: La función devuelve un objeto que contiene información 
# sobre la integración. Los campos más importantes son `t` (los puntos de tiempo 
#                                                           en los que se calculó la solución) y `y` (los valores de la solución en esos puntos de tiempo).

# # 5. **Uso en Modelado y Simulación**: `solve_ivp` es ampliamente utilizada 
# en ciencias e ingeniería para modelar sistemas dinámicos, como reacciones químicas, 
# movimientos mecánicos, dinámicas poblacionales, y en este caso, modelos económicos.




import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Definición de la función que representa la ecuación diferencial del modelo de Solow-Swan
def solow_model(t, k, s, alpha, n, d):
    return s * k**alpha - (n + d) * k

# Parámetros del modelo
s = 0.3      # Tasa de ahorro
alpha = 0.3  # Elasticidad de la producción
n = 0.01     # Tasa de crecimiento de la población
d = 0.05     # Tasa de depreciación del capital

# Condiciones iniciales
k0 = 0.5     # Capital inicial per cápita
t_span = (0, 100)  # Intervalo de tiempo
n_1 = 1000
t_eval = np.linspace(t_span[0], t_span[1], n_1)

# Resolución de la ecuación diferencial
sol = solve_ivp(solow_model, t_span, [k0], args=(s, alpha, n, d), method='RK45', t_eval=t_eval)

# Gráfico de la solución
plt.plot(sol.t, sol.y[0])
plt.title('Modelo de Crecimiento de Solow-Swan')
plt.xlabel('Tiempo')
plt.ylabel('Capital per cápita')
plt.grid(True)
plt.show()

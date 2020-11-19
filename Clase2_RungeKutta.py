# -*- coding: utf-8 -*-
"""
CLASE 2 - METODO DE INTEGRACION - RUNGE-KUTTA

El integrador ODEINT puede llegar a tener problemas, 
ya que internamente cambia entre métodos para resolver
la ecuación entre pasos temporales y a la vez va ajustando 
el paso (aunque solo nos diga la solución en los tiempos 
que se la pedimos) para tener el error acotado. 
Vean el siguiente ejemplo, con un campo vector bien inocente:
"""

import numpy as np
from scipy.integrate import odeint, ode
import matplotlib.pyplot as plt

# Sistema de ecuaciones
def f(t, z):
    x = z[0]
    y = z[1]
    dxdt = x-y
    dydt = x**2-4
    return [dxdt, dydt]

# Integracion odeint
dt = 0.01
tmax = 1
t = np.arange(0, tmax, dt)
plt.figure()
Xi = np.linspace(-4, 4, 4)
Yi = np.linspace(-4, 4, 4)
plt.figure()
for xi in Xi:
    for yi in Yi:
        zi = [xi, yi]
        solution_fut = odeint(f, zi, t, tfirst=True)
        xt = solution_fut[:, 0]
        yt = solution_fut[:, 1]
        plt.plot(xt, yt)
plt.title('Integracion por ODEINT')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()


"""En estos casos podemos usar otra estrategia en la que fijamos 
el método de integración. En vez de odeint vamos a usar un método 
bastante estandar, llamado [RUNGE-KUTTA 4]
(https://es.wikipedia.org/wiki/M%C3%A9todo_de_Runge-Kutta)

RK4 es el caballito de batalla de los integradores numéricos, 
pero, como todo, tiene sus ventajas y desventajas, 
y va a funcionar mejor o peor según el sistema.

Lo bueno de este método es que pueden escribirlo ustedes mismos
y no hay nada de caja negra! Para simplificar les vamos a proporcionar 
una versión que se adapta bastante bien si vienen de odeint.

Esta función ejecuta la integración de un paso temporal. 
Los argumentos que requiere son:
    i) campo vector (**función**) 
    ii) valor de las variables en el tiempo t 
    iii) paso temporal

Los últimos dos (*args, **kwargs) son para que, en caso de que sus 
campos vectores tengan argumentos, se los puedan pasar a la función 
y los sepa manejar (más, adelante)
"""

def rk4(dxdt, x, t, dt, *args, **kwargs):
    x = np.asarray(x)
    k1 = np.asarray(dxdt(t, x, *args, **kwargs))*dt
    k2 = np.asarray(dxdt(t, x + k1*0.5, *args, **kwargs))*dt
    k3 = np.asarray(dxdt(t, x + k2*0.5, *args, **kwargs))*dt
    k4 = np.asarray(dxdt(t, x + k3, *args, **kwargs))*dt
    return x + (k1 + 2*k2 + 2*k3 + k4)/6

"""Usemos el rk4 para el caso 2D y comparemos con odeint. 
Noten que el integrador nuevamente requiere que le pasemos 
el punto donde estamos como una lista y nos devuelve el x e y siguientes.

La forma de utilizarlo sería:
x[i+1], y[i+1] = rk4(campo_vector, [x[i], y[i]], tt, dt)
"""

# Integracion Runge-Kutta 4
dt = 0.01
tmax = 1
t = np.arange(0, tmax, dt)
plt.figure()
Xi = np.linspace(-4, 4, 4)
Yi = np.linspace(-4, 4, 4)
plt.figure()
for xi in Xi:
    for yi in Yi:
        # Definimos los vectores vacios
        xt = np.zeros_like(t)
        yt = np.zeros_like(t)
        # Definimos la condicion inicial
        xt[0], yt[0] = xi, yi

        # integro
        for i in range(len(t)-1):
            xt[i+1], yt[i+1] = rk4(f, [xt[i], yt[i]], t, dt)  

        # Ploteamos als soluciones
        plt.plot(xt, yt)
plt.title('Integracion por Runge-Kutta 4')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
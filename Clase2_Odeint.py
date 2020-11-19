# -*- coding: utf-8 -*-
"""
CLASE 2 - METODO DE INTEGRACION - Lib ODEINT

Hay diversos métodos, más o menos precisos y que funcionan 
para diversos sistemas. Scipy trae un integrador bastante 
bueno llamado ODEINT.

El odeint necesita que le digamos como calcular la derivada
en cada punto (tenemos que darle el campo vector), las condiciones 
iniciales y los tiempos donde queremos que integre.
"""

def dxdt(x, t):
    # nuestro sistema
    return -x**2 + 4

"""
odeint(campo vector, condiciones iniciales, vector de tiempos)
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

dt = 0.1
t = np.arange(0, 5, step=dt)
x0 = 10
solucion = odeint(dxdt, x0, t)  
#odeint hace "algo" y su output lo guardamos en la variable "solucion"
print(solucion.shape)
x = solucion[:, 0]
print(x)

"""Grafiquemos la solución:"""
plt.plot(t, x)

"""**Ojo con el dt**
Atención! Para odeint, el vector de tiempos solo le dice en qué 
momentos queremos que devuelva el resultado de la integración. 
El paso temporal real lo va a ir ajustando sin avisarnos!
Para convencernos comparemos 2 integraciones con tiempos muy distintos:
"""

# Graficamos la solución que teníamos de antes, con paso temporal "chico"
plt.plot(t, x, 'o-') #  para dt = 0.1

# Hacemos otra integración con paso temporal "grande"
dt = 1
t2 = np.arange(0, 5, step=dt)
x0 = 10
sol2 = odeint(dxdt, x0, t2)
x2 = sol2[:, 0]
plt.plot(t2, x2, 'o')

"""Ecuaciones con parámetros - Ejemplo Sigmoide"""
"""
x = odeint(campo_vector, xi, t, args=(parametro1, parametro2))

Para que esto funcione, nuestro campo vector tiene que saber 
como tomar esos parámetros! Por eso tenemos que definirlo con:

def campo_vector(x, t, parametro1, parametro2)

Veamos el ejemplo de la tasa de disparo en una neurona, 
donde el campo vector se definía como:
"""

def campo_vector(x, t, r, c):
    dxdt = -x + (1)/(1+np.e**(-(r+c*x)))
    return dxdt

# Definimos tiempo máximo, paso y un vector de tiempos
tmax = 50.
dt = 1./100
t = np.arange(0, tmax, dt)

# Le damos algún valor a los dos parámetros
r = -3
c = 6

# Nos preparamos varias condiciones iniciales
Xi = np.linspace(0, 2, 40)
plt.figure(figsize=(12,8))
# Evaluo todas las condiciones iniciales propuestas
for xi in Xi:
    # Para cada una de las condiciones iniciales hacemos la integración
    x = odeint(campo_vector, xi, t, args=(r, c))
    # Ploteamos. Python automáticamente va a ir cambiando el color en cada vuelta
    plt.plot(t, x)
plt.xlabel('t')
plt.ylabel('x')

# PARECE QUE TIENE 3 PTOS FIJOS, 2 TRACTORES (1 y 0) y 1 REPULSOR al rededor de 0.5

"""Ahora para un valor fijo de condición inicial, 
vemos qué pasa si cambiamos el valor de uno de los parámetros"""
# Nos armamos una lista de valores para r
rs = np.linspace(-3, -2, 10)
# Ponemos un única condición inicial
xi = 0.25
for r in rs:
    # Para cada valor del parámetro hacemos la integración
    x = odeint(campo_vector, xi, t, args=(r, c))
    # Graficamos y le ponemos una etiqueta a cada curva para reconocerlas
    plt.plot(t, x, label=r'r = {:.2f}; s = {:.2f}'.format(r, c))
# Le pedimos que nos muestre las etiquetas que generamos
plt.legend()

#%%

""""ODEINT IN 2D"""

def campo_vector(z, t):
    # Como ahora las variables vienen en una lista 
    # (en el primer argumento: z = [x,y])
    # primero las separamos para que sea más claro
    x = z[0]
    y = z[1]
    # Y ahora calculamos las derivadas
    dxdt = 4*x+2*y
    dydt = -17*x-5*y
    return [dxdt, dydt]

dt = 0.01
t = np.arange(0, 10, dt)
# Ponemos condiciones iniciales
xi = 0.1
yi = -0.2
# Y nos armamos una lista que contiene ci de cada variable
zi = [xi, yi]
# Llamamos al odeint y vean que le pasamos la lista de condiciones iniciales!
solution = odeint(campo_vector, zi, t)
# Vean como nos viene la solución:
plt.plot(solution)
print(solution.shape)
print(solution)

# Cada elemento que nos devuelve es un par de coordenadas [x, y]
# Para recuperar las x por un lado y las y por el otro:
xt = solution[:, 0]
yt = solution[:, 1]
plt.plot(xt, yt)
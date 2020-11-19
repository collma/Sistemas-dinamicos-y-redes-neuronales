# -*- coding: utf-8 -*-
"""
CLASE 2 - METODO DE INTEGRACION DE EULER - CAMPO VECTOR
"""

import numpy as np

# FUNCION DERIVADAS
def ecuaciones(x,y, a, b, c, d):
    '''
    Recibe:
       x, y: Variables del sistema
       param: Lista con los parámetros del sistema
    Devuelve:
       x_dot, y_dot: valor de las derivadas para cada variable
    '''
    
    x_dot = a*x + b*y
    y_dot = c*x + d*y

    return x_dot, y_dot

# FUNCION DE INTEGRACION
def integrar_ecuaciones(total_time,dt,X0,a, b, c, d):

    '''
    Recibe:
       total_time: Tiempo total del integración
       dt: Paso temporal (h del método)
       X0: Lista con [x0,y0] valores iniciales de la integración
       params: Lista con los parámetros del sistema
    Devuelve:
       x_s, y_s: Vectores con las soluciones para ambas variables
       num_steps: Numero de pasos de integracion
    '''

    num_steps = int(np.divide(total_time,dt))

    # Empty vectors
    xs = np.empty(num_steps)
    ys = np.empty(num_steps)

    # Set initial values
    xs[0], ys[0] = X0

    # Empty vectors
    x_dot = np.empty(num_steps)
    y_dot = np.empty(num_steps)

    # Set initial derivatives values
    x_dot[0], y_dot[0] = ecuaciones(xs[0], ys[0], a, b, c, d)

    # Integramos con método de Euler
    for i in range(num_steps-1):
        xs[i+1] = xs[i] + dt*x_dot[i]
        ys[i+1] = ys[i] + dt*y_dot[i]

        x_dot[i+1], y_dot[i+1] = ecuaciones(xs[i+1], ys[i+1], a, b, c, d)

    return xs, ys, num_steps

# Definimos el paso de integracion
dt = 0.05
# Definimos el tiempo total de integracion
total_time = 5

# Parametros
a = 4 # Si a = 4 ATRACTOR y a = 5 REPULSOR
b = 2
c = -17
d = -5

# Definimos la condicion inicial
X0 = (1.5,0.0)

# Integramos
x, y, num_steps = integrar_ecuaciones(total_time,dt,X0, a, b, c, d)

#Definimos el vector de tiempos y los vectores x, y que iremos llenando
t = np.arange(0, total_time, step=dt)

# GRAFICAMOS EL ESPACIO DE FASES

import matplotlib.pyplot as plt

# Definimos la figura que contendra todos los resultados
plt.figure(figsize=(15,5))

# Definimos un primer grafico dentro de la figura
plt.subplot(131) # 1 fila, 3 columnas, primer grafico
# Ploteamos x vs y en colore darkcyan
plt.plot(x, y, 'darkcyan')
# Ponemos el nombre a los ejes
plt.xlabel("x", fontsize=15)
plt.ylabel("y", fontsize=15, rotation=0, labelpad=20)

# Repetimos para un segundo gráfico
plt.subplot(132) # 1 fila, 3 columnas, segundo grafico
plt.plot(t, x, 'darkred')
plt.xlabel("tiempo", fontsize=15)
plt.ylabel("x", rotation=0, fontsize=15)

# Repetimos para un tercer gráfico
plt.subplot(133) # 1 fila, 3 columnas, tercer grafico
plt.plot(t, y, 'k')
plt.xlabel("tiempo", fontsize=15)
plt.ylabel("y", rotation=0, fontsize=15)

plt.show()

# GRAFICAMOS EL CAMPO VECTOR

#Damos la grilla de puntos sobre la que miraremos el campo vector
x_grilla, y_grilla= np.meshgrid(np.linspace(-2, 2, 20),np.linspace(-6, 6, 24))
dx_grilla, dy_grilla = ecuaciones(x_grilla,y_grilla, a, b, c, d)

print(np.shape(dx_grilla)) #Para ver cuantas filas y columnas
print(dx_grilla[0][:]) #Miramos la primera fila, todas las columnas

#Ahora las graficamos; usamos quiver de matplotlib -> chusmear la documentacion
fig, ax = plt.subplots(figsize=(8,8))
ax.set_title("campo vector")
ax.quiver(x_grilla, y_grilla, dx_grilla, dy_grilla, color='k', angles='xy')
ax.set_xlabel('x', fontsize=15)
ax.set_ylabel('y', fontsize=15)
ax.plot(x, y)
plt.show()
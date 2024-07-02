# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Vinícius Assumpcção de Araújo - 200028472

import numpy as np

# Define o sistema de 
def dydx_system(x, y):
    y1, y2 = y
    dy1dx = y2
    dy2dx = -4*y2 - 3*y1 - x
    return np.array([dy1dx, dy2dx])

# Implementacao do metodo de Euler Explícito
def euler_explicit_system(dydx, x0, y0, x_end, step):
    N = int((x_end - x0) / step) + 1  # Numero de passos
    x = np.linspace(x0, x_end, N)
    y = np.zeros((N, len(y0))) # Valor inicial para cada equacao
    y[0] = y0  # Condicao inicial
    
    for i in range(1, N):
        y[i] = y[i-1] + step * dydx(x[i-1], y[i-1])
    
    return x, y

# Condicoes iniciais
y0 = np.array([4/9, 7/3])

# Define parametros
x0 = 0.0
x_end = 2.0
step = 0.5

x_values, y_values = euler_explicit_system(dydx_system, x0, y0, x_end, step)

print('valores de x: ',  x_values,'valores de y: ',  y_values)

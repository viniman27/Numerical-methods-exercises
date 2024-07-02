# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Vinícius Assumpcção de Araújo - 200028472


import numpy as np

# Define a equacao diferencial
def dydx(y):
    return -y**2

# Implementacao do metodo de Euler Explícito
def euler_explicit(dydx, x0, y0, x_end, step):
    N = int((x_end - x0) / step) + 1  # Numero de passos
    x = np.linspace(x0, x_end, N)
    y = np.zeros(N)
    y[0] = y0  # condicao inicial
    
    for i in range(1, N):
        y[i] = y[i-1] + step * dydx(y[i-1])
    
    return x, y

# Define parametros
x0 = 1.0
y0 = 1.0
x_end = 3.0
step = 0.5

x_values, y_values = euler_explicit(dydx, x0, y0, x_end, step)

# Solucao da equacao y' = -y^2 with y(1) = 1 is y = 1/x
# Calcula os valores exatos de y e os erros percentuais
exact_y_values = 1 / x_values
percentage_errors = np.abs((y_values - exact_y_values) / exact_y_values) * 100

print('valores de x: ', x_values, 'valores de y: ',  y_values, 'valores de y exatos: ',  exact_y_values,'erros percentuais: ',  percentage_errors)

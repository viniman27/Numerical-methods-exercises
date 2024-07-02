# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Vinícius Assumpcção de Araújo - 200028472

import numpy as np

# Define a equacao diferencial
def dydx(x, y):
    return 2*y / (x + 1) + (x + 1)**3

# Define o metodo de Runge-Kutta de quarta ordem
def runge_kutta(dydx, x0, y0, x_end, step):
    N = int((x_end - x0) / step) + 1  # Numero de passos
    x = np.linspace(x0, x_end, N)
    y = np.zeros(N)
    y[0] = y0  # Condicso inicial
    
    for i in range(N - 1):
        k1 = step * dydx(x[i], y[i])
        k2 = step * dydx(x[i] + step / 2, y[i] + k1 / 2)
        k3 = step * dydx(x[i] + step / 2, y[i] + k2 / 2)
        k4 = step * dydx(x[i] + step, y[i] + k3)
        
        y[i + 1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return x, y

# Define a solucso exata
def exact_solution(x):
    return 0.5 * ((x + 1)**4 + 5 * (x + 1)**2)

# Parametros iniciais
x0 = 0.0
y0 = -3.0
x_end = 2.0
step = 0.5

x_values, y_rk = runge_kutta(dydx, x0, y0, x_end, step)

# Calcula os valores exatos e os erros percentuais
y_exact = exact_solution(x_values)
percentage_errors = np.abs((y_rk - y_exact) / y_exact) * 100

# Print the results
print("x values:", x_values)
print("Runge-Kutta y values:", y_rk)
print("Exact y values:", y_exact)
print("Percentage relative errors:", percentage_errors)


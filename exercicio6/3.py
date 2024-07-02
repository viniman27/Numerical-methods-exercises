# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Vinícius Assumpcção de Araújo - 200028472

import numpy as np

# Define a função para integrar
def f(x):
    return np.exp(x)  # e^x

# Define o tamanho do passo
h = 1/10  # h é o incremento no cálculo numérico da integral
# Define o número de intervalos
n = int(1/h)  # número de subintervalos baseado no tamanho do passo

# Função da regra dos trapézios
def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n  # recalcula h com base no número de intervalos (caso n tenha mudado)
    x_values = np.linspace(a, b, n+1)  # gera valores de x igualmente espaçados entre a e b
    y_values = func(x_values)  # calcula valores de y para cada x
    # Calcula a aproximação da integral pela regra dos trapézios
    return h * (0.5 * y_values[0] + sum(y_values[1:-1]) + 0.5 * y_values[-1])

# Função da regra 1/3 de Simpson
def simpson_one_third_rule(func, a, b, n):
    # A regra de Simpson requer um número par de intervalos
    if n % 2 == 1:
        n += 1  # ajusta n para ser par, se necessário
    h = (b - a) / n  # recalcula h
    x_values = np.linspace(a, b, n+1)  # gera valores de x
    y_values = func(x_values)  # calcula valores de y
    # Calcula a aproximação da integral pela regra 1/3 de Simpson
    return (h/3) * (y_values[0] + 4 * sum(y_values[1:n:2]) + 2 * sum(y_values[2:n-1:2]) + y_values[n])

# Calcula a aproximação usando a regra dos trapézios
trapezoidal_approx = trapezoidal_rule(f, 0, 1, n)

# Calcula a aproximação usando a regra 1/3 de Simpson
simpson_approx = simpson_one_third_rule(f, 0, 1, n)

# Exibe os resultados
print(f"Aproximação pela regra dos Trapézios: {trapezoidal_approx}")
print(f"Aproximação pela regra 1/3 de Simpson: {simpson_approx}")

# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Vinícius Assumpcção de Araújo - 200028472

import numpy as np

# Define a função para integração
def f(x):
    return np.exp(-x)  # e^-x

# Tamanho do passo
h = 1/10  # h é o intervalo entre os pontos de amostra

# Número de intervalos, ajustado para ser um múltiplo de 3 para a regra 3/8 de Simpson
n = int(0.9/h)  # Calcula o número de intervalos baseado no comprimento total do intervalo e no passo h
if n % 3 != 0:
    n += 3 - (n % 3)  # Ajusta n para garantir que seja múltiplo de 3

# Função da regra 3/8 de Simpson
def simpson_three_eighths_rule(func, a, b, n):
    # Garante que n seja um múltiplo de 3
    if n % 3 != 0:
        raise ValueError("n deve ser múltiplo de 3 para a regra 3/8 de Simpson.")
    h = (b - a) / n  # Define o novo passo baseado no número de intervalos
    x_values = np.linspace(a, b, n+1)  # Gera valores de x linearmente espaçados entre a e b
    y_values = func(x_values)  # Calcula os valores de y para cada x
    # Aplica a regra 3/8 de Simpson para calcular a aproximação da integral
    return (3 * h / 8) * (y_values[0] + y_values[-1] + 3 * sum(y_values[1:-1:3]) + 3 * sum(y_values[2:-1:3]) + 2 * sum(y_values[3:n-2:3]))

# Calcula a aproximação usando a regra 3/8 de Simpson
simpson_three_eighths_approx = simpson_three_eighths_rule(f, 0, 0.9, n)

# Imprime o resultado
print(f"Aproximação pela regra 3/8 de Simpson: {simpson_three_eighths_approx}")

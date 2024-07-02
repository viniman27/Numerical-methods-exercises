# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Vinícius Assumpcção de Araújo - 200028472

import sympy as sp

# Define a variável e a função para integração
x = sp.symbols('x')  # Cria um símbolo x para usar em expressões simbólicas
f = 3*x**3 - 3*x + 1  # Define a função f(x) = 3x^3 - 3x + 1

# Calcula o valor exato da integral
exact_integral = sp.integrate(f, (x, 0, 4))  # Integra f(x) de 0 a 4 simbolicamente

# Converte a expressão simbólica f para uma função que pode ser avaliada numericamente
f_num = sp.lambdify(x, f, 'numpy')

# Define o número de subintervalos para a regra dos trapézios
n_intervals = 4

# Corrige a função da regra dos trapézios para trabalhar diretamente com valores numéricos
def trapezoidal_rule_numerical(func, a, b, n):
    h = (b - a) / n  # Calcula a largura de cada subintervalo
    x_values = [a + i * h for i in range(n + 1)]  # Gera os valores de x em cada subintervalo
    y_values = [func(x) for x in x_values]  # Calcula os valores de f(x) para cada x
    return h * (0.5 * y_values[0] + sum(y_values[1:-1]) + 0.5 * y_values[-1])  # Aplica a regra dos trapézios

# Aplica a regra dos trapézios corrigida para aproximar a integral usando a função numérica
approx_integral = trapezoidal_rule_numerical(f_num, 0, 4, n_intervals)

# Calcula o erro numérico
error = exact_integral - approx_integral  # O erro é a diferença entre o valor exato e o valor aproximado

# Exibe o valor exato, o valor aproximado e o erro calculado, todos avaliados como números de ponto flutuante
exact_integral.evalf(), approx_integral, error.evalf()

# Exibe o valor exato da integral
print(f"Valor exato da integral: {exact_integral.evalf()}")

# Exibe o valor aproximado da integral usando a regra dos trapézios
print(f"Valor aproximado pela regra dos trapézios: {approx_integral}")

# Exibe o erro cometido na aproximação
print(f"Erro da aproximação: {error.evalf()}")


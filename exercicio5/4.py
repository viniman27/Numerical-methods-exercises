# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Vinícius Assumpcção de Araújo - 200028472

import sympy as sp

# Definicao dos simbolos
t = sp.symbols('t')

# Ddos
time = [1, 5, 8]
volume = [1, 8, 16.4]

# Definir o polinomio pro lagrange
def lagrange_basis(t_values, i, t):
    basis = 1
    for j, tj in enumerate(t_values):
        if j != i:
            basis *= (t - tj) / (t_values[i] - tj)
    return basis

# Construir o polinomio interpolador de lagrange
P = sum(volume[i] * lagrange_basis(time, i, t) for i in range(len(time)))

# Calculara derivada
P_derivative = sp.diff(P, t)

# Avaliar a derivada no instante 7s
derivative_at_7 = P_derivative.subs(t, 7)

print("Polinomio: ",P," Derivada do polinomio: ", P_derivative," Derivada no instante 7: ", derivative_at_7)

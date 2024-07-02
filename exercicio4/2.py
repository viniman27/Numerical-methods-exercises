# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Viniícius Assumpcçaão de Arauúujo - 200028472


import numpy as np

# Dados
x = [-1.0, -0.75, -0.6, -0.5, -0.3, 0, 0.2, 0.4, 0.5, 0.7, 1]
y = [2.05, 1.153, 0.45, 0.4, 0.5, 0, 0.2, 0.6, 0.512, 1.2, 2.05]

# Calcular os elementos da matriz A e B
A = np.array([
    [len(x), sum(x), sum(np.power(x, 2))],
    [sum(x), sum(np.power(x, 2)), sum(np.power(x, 3))],
    [sum(np.power(x, 2)), sum(np.power(x, 3)), sum(np.power(x, 4))]
])

B = np.array([
    sum(y),
    sum(y * np.array(x)),
    sum(y * np.array(np.power(x, 2)))
])

# Calcular os coeficientes
a0, a1, a2 = np.linalg.solve(A, B)

print("a0:", a0)
print("a1:", a1)
print("a2:", a2)

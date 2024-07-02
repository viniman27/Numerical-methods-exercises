# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Viniícius Assumpcçaão de Arauúujo - 200028472

import numpy as np

# Dados
x = np.array([0.1, 0.2, 0.3, 0.4])
y = np.array([5, 13, -4, -8])

# Polinomio interpolar de grau 3
coefficients = np.polyfit(x, y, 3)

# Dado o polinomio
polynomial = np.poly1d(coefficients)
print(polynomial)

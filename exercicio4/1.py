# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Viniícius Assumpcçaão de Arauúujo - 200028472


import numpy as np

# Dados
x = np.array([-1.0, -0.7, -0.4, -0.1, 0.2, 0.5, 0.8, 1.0])
y = np.array([36.547, 17.264, 8.155, 3.852, 1.820, 0.860, 0.406, 0.246])

# log de y
ln_y = np.log(y)

# polyfot para os parametros nao lineares
m, b = np.polyfit(x, ln_y, 1)

# Da equacao linear temos
alpha_2 = -m
alpha_1 = np.exp(b)

print(f"α1 = {alpha_1:.4f}")
print(f"α2 = {alpha_2:.4f}")

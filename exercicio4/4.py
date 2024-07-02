# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Viniícius Assumpcçaão de Arauúujo - 200028472


x_points = [-1, 0, 2]
y_points = [4, 1, -1]

def lagrange_basis(x, x_points, k):
    """Calcula o k-ésimo polinômio base de Lagrange."""
    product = 1
    for i, xi in enumerate(x_points):
        if i != k:
            product *= (x - xi) / (x_points[k] - xi)
    return product

def lagrange_interpolation(x, x_points, y_points):
    """Calcula o polinômio interpolador de Lagrange."""
    L = 0
    for k, yk in enumerate(y_points):
        L += yk * lagrange_basis(x, x_points, k)
    return L

# Calculando o valor em x=1
value_at_x1 = lagrange_interpolation(1, x_points, y_points)
print(f"O valor de f(1) é: {value_at_x1}")

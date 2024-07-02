import numpy as np

# Coeficientes do sistema
A = np.array([[3.0, 2.0, 4.0],
              [1.0, 1.0, 2.0],
              [4.0, 3.0, -2.0]], dtype=float)

# Termos constantes
b = np.array([1.0, 2.0, 3.0], dtype=float)

# Tamanho do sistema
n = len(b)

# Inicialização da matriz LU
LU = np.zeros((n, n))
for i in range(n):
    LU[i, i] = 1.0

# Eliminação de Gauss com decomposição LU
for k in range(n-1):
    for i in range(k+1, n):
        factor = A[i, k] / A[k, k]
        LU[i, k] = factor
        for j in range(k, n):
            A[i, j] -= factor * A[k, j]

# Resolução do sistema LUx = b
# Primeiro, resolvemos Ly = b
y = np.zeros(n)
y[0] = b[0]
for i in range(1, n):
    y[i] = b[i] - np.dot(LU[i, :i], y[:i])

# Em seguida, resolvemos Ux = y
x = np.zeros(n)
x[n-1] = y[n-1] / A[n-1, n-1]
for i in range(n-2, -1, -1):
    x[i] = (y[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

# Arredondamento para 6 algarismos significativos
x = np.round(x, 6)

# Saída dos resultados
print("Solução:")
for i in range(n):
    print(f"x{i+1} = {x[i]}")

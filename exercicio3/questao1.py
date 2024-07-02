import numpy as np

# Coeficientes do sistema
A = np.array([[3.0, 2.0, 4.0],
              [1.0, 1.0, 2.0],
              [4.0, 3.0, -2.0]])

# Termos constantes
b = np.array([1.0, 2.0, 3.0])

# Tamanho do sistema
n = len(b)

# Eliminação de Gauss
for k in range(n-1):
    for i in range(k+1, n):
        factor = A[i, k] / A[k, k]
        for j in range(k, n):
            A[i, j] -= factor * A[k, j]
        b[i] -= factor * b[k]

# Resolução retroativa
x = np.zeros(n)
x[n-1] = b[n-1] / A[n-1, n-1]
for i in range(n-2, -1, -1):
    sum = b[i]
    for j in range(i+1, n):
        sum -= A[i, j] * x[j]
    x[i] = sum / A[i, i]

# Arredondamento para 6 algarismos significativos
x = np.round(x, 6)

# Saída dos resultados
print("Solução:")
for i in range(n):
    print(f"x{i+1} = {x[i]}")

import numpy as np

# Coeficientes do sistema
A = np.array([[5.0, 1.0, 1.0],
              [3.0, 4.0, 1.0],
              [3.0, 3.0, 6.0]])

# Termos constantes
b = np.array([5.0, 6.0, 0.0])

# Tamanho do sistema
n = len(b)

# Valor inicial
x0 = np.array([0.0, 0.0, 0.0])

# Tolerância
tolerance = 5e-2

# Número máximo de iterações
max_iterations = 1000

# Inicialização do vetor de solução
x = x0.copy()

# Inicialização do erro relativo estimado
error = float('inf')

# Iterações do método de Gauss-Seidel
for k in range(max_iterations):
    x_new = x.copy()
    for i in range(n):
        x_new[i] = (b[i] - np.dot(A[i, :i], x_new[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    # Cálculo do erro relativo estimado
    error = np.max(np.abs(x_new - x) / np.maximum(np.abs(x_new), np.ones(n)))
    # Atualização da solução
    x = x_new
    if error < tolerance:
        break

# Arredondamento para 6 algarismos significativos
x = np.round(x, 6)

# Saída dos resultados
print("Solução:")
for i in range(n):
    print(f"x{i+1} = {x[i]}")


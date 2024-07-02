import sympy as sp

# Define the symbol α
alpha = sp.symbols('alpha')

# Define the 17x17 matrix for the system
A = sp.Matrix([
    [-alpha, 0, 1, alpha, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-alpha, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ... Continue this for all the rows
])

# Define the column matrix of the results
b = sp.Matrix([
    [0],
    [0],
    [0],
    [100000],
    [0],
    [0],
    [0],
    [150000],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [100000],
    [0],
])

# Solve using Gaussian Elimination
x = A.LUsolve(b)

# Print the solutions
print("Solutions using Gaussian Elimination:")
print(x)

# LU Decomposition using Crout's method
L, U, _ = A.LUdecomposition(method="Crout")
y = L.LUsolve(b)
x2 = U.LUsolve(y)

# Print the solutions using Crout's method
print("\nSolutions using Crout's method:")
print(x2)

import numpy as np

def jacobi(A, b, x0, tol=1e-6, max_iter=1000):
    n = len(b)
    x = np.zeros_like(x0)
    for it in range(max_iter):
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i,:i], x0[:i]) - np.dot(A[i,i+1:], x0[i+1:])) / A[i,i]
        if np.linalg.norm(x - x0) < tol:
            return x
        x0 = x.copy()
    return x

A = np.array([
    [4, -1, 0, -1, 0, 0, 0, 0, 0, 0],
    [-1, 4, -1, 0, -1, 0, 0, 0, 0, 0],
    [0, -1, 4, 0, 0, -1, 0, 0, 0, 0],
    [-1, 0, 0, 4, -1, 0, 0, 0, 0, 0],
    [0, -1, 0, -1, 4, -1, -1, 0, 0, 0],
    [0, 0, -1, 0, -1, 4, 0, -1, 0, 0],
    [0, 0, 0, 0, -1, 0, 4, -1, -1, 0],
    [0, 0, 0, 0, 0, -1, -1, 4, -1, -1],
    [0, 0, 0, 0, 0, 0, -1, -1, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, -1, 0, 4]
])
b = np.array([-110, -30, -40, -110, 0, -15, -90, -25, -55, -65])
x0 = np.array([20, 20, 20, 20, 20, 20, 20, 20, 20, 20])

sol_jacobi = jacobi(A, b, x0)
print("Solução pelo método de Jacobi:", sol_jacobi)


def gauss_seidel(A, b, x0, tol=1e-6, max_iter=1000):
    L = np.tril(A)
    U = A - L
    x = x0
    for i in range(max_iter):
        x_new = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    return x

sol_gauss_seidel = gauss_seidel(A, b, x0)
print("Solução pelo método de Gauss-Seidel:", sol_gauss_seidel)

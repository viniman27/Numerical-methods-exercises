# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Vinícius Assumpcção de Araújo - 200028472


import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Dados
time = np.array([1, 2, 3.25, 4.5, 6, 7, 8, 8.5, 9.3, 10])
velocity = np.array([10, 12, 11, 14, 17, 16, 12, 14, 14, 10])

# Calculo do polinomio
coefs = np.polyfit(time, velocity, 2)
quadratic_polynomial = Polynomial(coefs[::-1]) 

# Derivada do polinomio
acceleration_polynomial = quadratic_polynomial.deriv()

# Calculo das aceleracoes
accelerations = acceleration_polynomial(time)


print(f"Os coeficientes sao: {coefs}")

print(f"As aceleracoes sao: {accelerations}")

# Plotando
plt.figure(figsize=(10, 5))
# Pontoas de velocidade original
plt.scatter(time, velocity, color='blue', label='Data points')
# Regressao quadratica
t_line = np.linspace(min(time), max(time), 200)
plt.plot(t_line, quadratic_polynomial(t_line), color='red', label='Quadratic fit')
# Pontos de aceleracao
plt.scatter(time, quadratic_polynomial(time), color='green', label='Acceleration points', zorder=5)

plt.title('Regrssao quadratica sobre o tempo')
plt.xlabel('Time (t)')
plt.ylabel('Velocity (v) and Acceleration (a)')
plt.legend()
plt.grid(True)
plt.show()

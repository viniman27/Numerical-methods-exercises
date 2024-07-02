# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Vinícius Assumpcção de Araújo - 200028472


import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


# Letra a

# Dados
time = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16])
position = np.array([0, 0.7, 1.8, 3.4, 5.1, 6.3, 7.3, 8.0, 8.4])

# Interpolando
cubic_interp = interp1d(time, position, kind='cubic')

# Usando diferenças finitas

dt = 2 
velocity_at_10 = (cubic_interp(10 + dt) - cubic_interp(10 - dt)) / (2 * dt)

acceleration_at_10 = (cubic_interp(10 - dt) - 2 * cubic_interp(10) + cubic_interp(10 + dt)) / dt**2

print("velocidade(a): ",velocity_at_10," aceleracao(a): ",acceleration_at_10)

# Letra b

# Funcao para calcular as derivadas
def forward_finite_difference_first_derivative(x, h):
    
    return (-3*x[0] + 4*x[1] - x[2]) / (2*h)

def forward_finite_difference_second_derivative(x, h):
   
    return (-2*x[0] + 5*x[1] - 4*x[2] + x[3]) / h**2


h = 2 
first_derivative_points = position[4:7] 
second_derivative_points = position[4:8] 

# Primeira e segunda derivada
velocity_forward = forward_finite_difference_first_derivative(first_derivative_points, h)
acceleration_forward = forward_finite_difference_second_derivative(second_derivative_points, h)

print( "velocidade(b): ", velocity_forward," aceleracao(b): ",  acceleration_forward)


# Letra c

def backward_finite_difference_first_derivative(x, h):

    return (x[2] - 4*x[1] + 3*x[0]) / (2*h)

def backward_finite_difference_second_derivative(x, h):

    return (2*x[3] - 5*x[2] + 4*x[1] - x[0]) / h**2


first_derivative_points_backward = position[3:6] 
second_derivative_points_backward = position[3:7] 


velocity_backward = backward_finite_difference_first_derivative(first_derivative_points_backward, h)
acceleration_backward = backward_finite_difference_second_derivative(second_derivative_points_backward, h)

print("velocidade(c): ",velocity_backward," aceleracao(c): ", acceleration_backward)

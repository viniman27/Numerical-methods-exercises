import math

# Função para calcular a corrente Im em função de W (frequência angular)
def current_equation(W, R, L, C, Vm):
    return Vm / math.sqrt(R**2 + ((W*L - 1)/(W*C))**2)

# Método da bissecção para encontrar a frequência f
def bissection_method(R, L, C, Vm, Im, a, b, tolerance):
    fa = current_equation(2*math.pi*a, R, L, C, Vm) - Im
    fb = current_equation(2*math.pi*b, R, L, C, Vm) - Im

    if fa * fb >= 0:
        raise Exception("O método da bissecção não é aplicável a este intervalo. Escolha um novo intervalo [a, b] inicial.")

    while (b - a) / 2.0 > tolerance:
        c = (a + b) / 2.0
        fc = current_equation(2*math.pi*c, R, L, C, Vm) - Im

        if fc == 0.0:
            return c  # Encontrou a raiz exata
        elif fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc

    return (a + b) / 2.0

# Método da secante para encontrar a frequência f
def secant_method(R, L, C, Vm, Im, x0, x1, tolerance):
    f0 = current_equation(2*math.pi*x0, R, L, C, Vm) - Im
    f1 = current_equation(2*math.pi*x1, R, L, C, Vm) - Im

    while abs(f1) > tolerance:
        if f1 - f0 == 0:
            raise Exception("A divisão por zero ocorreu. Escolha novos valores iniciais.")
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        x0, x1 = x1, x2
        f0, f1 = f1, current_equation(2*math.pi*x2, R, L, C, Vm) - Im

    return x1

# Parâmetros do problema
R = 140.92
L = 260e-3  # Convertendo para Henrys
C = 25e-6   # Convertendo para Farads
Vm = 24
Im = 0.15
tolerance = 0.0001

# Intervalo de busca inicial para o método da bissecção
a = 0.1
b = 10000.0

# Valores iniciais para o método da secante
x0 = 1.0
x1 = 10.0

# Encontrar a frequência usando o método da bissecção
try:
    f_bissec = bissection_method(R, L, C, Vm, Im, a, b, tolerance)
    print(f"Frequência (Método da Bissecção): {f_bissec} Hz")
except Exception as e:
    print(e)

# Encontrar a frequência usando o método da secante
try:
    f_secant = secant_method(R, L, C, Vm, Im, x0, x1, tolerance)
    print(f"Frequência (Método da Secante): {f_secant} Hz")
except Exception as e:
    print(e)

def funcao(x):
    return x**2 + x - 6

def iteracao_1(x):
    return (6 - x)**0.5

def iteracao_2(x):
    return 6 - x**2

def iteracao_3(x):
    return x - (x**2 + x - 6) / (2*x + 1)

def iteracao_4(x):
    return x - (x**2 + x - 6) / 1

# Valor inicial
x = 1.5

# Realiza cinco iterações para cada função de iteração
for i in range(5):
    x = iteracao_1(x)
    print(f"Iteração {i+1} (Função 1): x = {x}")

x = 1.5  # Redefine o valor inicial

for i in range(5):
    x = iteracao_2(x)
    print(f"Iteração {i+1} (Função 2): x = {x}")

x = 1.5  # Redefine o valor inicial

for i in range(5):
    x = iteracao_3(x)
    print(f"Iteração {i+1} (Função 3): x = {x}")

x = 1.5  # Redefine o valor inicial

for i in range(5):
    x = iteracao_4(x)
    print(f"Iteração {i+1} (Função 4): x = {x}")

# Define a função que representa a equação f(x)
def funcao(x):
    return x**3 - 9*x + 3

# Implementa o método da bissecção
def bisseccao(funcao, a, b, tolerancia):
    # Verifica se a função tem mudança de sinal no intervalo [a, b]
    if funcao(a) * funcao(b) >= 0:
        raise ValueError("A função não muda de sinal no intervalo dado.")
    
    # Loop até a tolerância ser atingida
    while (b - a) / 2 > tolerancia:
        # Calcula o ponto médio do intervalo [a, b]
        c = (a + b) / 2
        
        # Se a função retorna exatamente 0 no ponto médio, retornamos o resultado
        if funcao(c) == 0:
            return c
        # Caso contrário, ajustamos os limites a e b com base no sinal da função em c
        elif funcao(c) * funcao(a) < 0:
            b = c
        else:
            a = c
    
    # Retorna a estimativa da raiz como a média entre a e b
    return (a + b) / 2

# Intervalo inicial [a, b]
a = 0
b = 1

# Tolerância desejada
tolerancia = 1e-3

# Chama a função bisseccao para encontrar a raiz
raiz = bisseccao(funcao, a, b, tolerancia)

# Imprime o resultado
print("A raiz aproximada é:", raiz)

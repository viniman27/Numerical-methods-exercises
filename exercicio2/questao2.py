def funcao(x):
    return x**3 - 9*x + 3

def falsa_posicao(funcao, a, b, tolerancia, max_iter):
    iteracao = 0
    while iteracao < max_iter:
        # Calcula os valores da função nos pontos a e b
        fa = funcao(a)
        fb = funcao(b)
        
        # Calcula a próxima estimativa da raiz usando a interpolação linear
        c = (a * fb - b * fa) / (fb - fa)
        
        # Calcula o valor da função no ponto c
        fc = funcao(c)
        
        # Verifica se a raiz foi encontrada com a tolerância desejada
        if abs(fc) < tolerancia:
            return c
        
        # Atualiza os limites a e b com base no valor da função em c
        if fa * fc < 0:
            b = c
        else:
            a = c
        
        iteracao += 1
    
    # Se atingir o número máximo de iterações sem convergência, retorna None
    return None

# Intervalo inicial
a = 0
b = 1

# Tolerância desejada
tolerancia = 5e-4

# Número máximo de iterações
max_iter = 1000

# Chama a função falsa_posicao para encontrar a raiz
raiz = falsa_posicao(funcao, a, b, tolerancia, max_iter)

if raiz is not None:
    print("A raiz aproximada é:", raiz)
else:
    print("O método não convergiu dentro do número máximo de iterações.")

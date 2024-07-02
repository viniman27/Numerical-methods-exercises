# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Viniícius Assumpcçaão de Arauúujo - 200028472

def interpolacaoNewton(x, y):
    n = len(x)
    
    tabelaDiferencas = [y]
    for i in range(1, n):
        listaDiferencas = []
        for j in range(n - i):
            diferenca = (tabelaDiferencas[i-1][j+1] - tabelaDiferencas[i-1][j]) / (x[j+i] - x[j])
            listaDiferencas.append(diferenca)
        tabelaDiferencas.append(listaDiferencas)

    def polinomioInterpolador(z):
        resultado = y[0]
        produtoTermos = 1
        for i in range(1, n):
            produtoTermos *= (z - x[i-1])
            resultado += produtoTermos * tabelaDiferencas[i][0]
        return resultado

    return polinomioInterpolador

x = [-1, 0, 1, 2, 3]
y = [1, 1, 0, -1, -2]

polinomioInterpolador = interpolacaoNewton(x, y)

for xi in x:
    print(f"P({xi}) = {polinomioInterpolador(xi)}")
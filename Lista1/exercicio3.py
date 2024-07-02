from math import sqrt

#letra A 

# f(0.005)≈0.33333333

# letra B:

# Valor calculado de f(x)
f_x = 0.333333

# Valor verdadeiro de f(x)
true_f_x = 1 / 3

# Calcular o erro relativo real
relative_error = abs(f_x - true_f_x) / abs(true_f_x)

# Exibir o erro relativo real
print("Erro relativo real:", relative_error)

# letra C

# Defina o valor de x
x = 0.005

# Calcule f(x) original
f_x_original = (sqrt(9 + x) - 3) / x

# Calcule f(x) usando a forma menos propensa a erros de arredondamento
f_x_melhorada = ((sqrt(9 + x) + 3) / (sqrt(9 + x) + 3)) * f_x_original

# Exiba os valores com seis algarismos significativos
print("f(x) original:", round(f_x_original, 6))
print("f(x) melhorada:", round(f_x_melhorada, 6))

## Conclusao: a forma menos propensa é muito boa para otimizar cálculos computacionais,
# mas os resultados que foram obtidos anteriormente sao muito próximos, se comparados com a forma menos propensa.

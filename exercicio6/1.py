# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Vinícius Assumpcção de Araújo - 200028472

# Valores dados obtidos a partir da saída OCR
x_values = [0.0, 0.2, 0.4, 0.6, 0.8]  # Valores de x
f_values = [1.0, 1.2408, 1.5735, 2.0333, 2.6965]  # Valores de f(x) correspondentes aos valores de x

# Calcula delta x, assumindo espaçamento uniforme
delta_x = x_values[1] - x_values[0]  # Calcula o intervalo entre valores consecutivos de x

# Regra do retângulo usando pontos médios
# Para a regra do retângulo usando pontos médios, tomamos a média de f(x) nos pontos finais de cada subintervalo
rectangle_rule_sum = sum((f_values[i] + f_values[i + 1]) / 2 for i in range(len(f_values) - 1)) * delta_x

# Regra do ponto médio
# Para a regra do ponto médio, usamos apenas os pontos médios dos intervalos. Portanto, calcularíamos f(x) em x = 0.1, 0.3, 0.5, 0.7
# Como não temos a função f(x), aproximamos isso tomando a média de f(x) nos pontos finais de cada subintervalo
midpoint_values = [(f_values[i] + f_values[i + 1]) / 2 for i in range(len(f_values) - 1)]
midpoint_rule_sum = sum(midpoint_values) * delta_x

# Os resultados obtidos para a soma pela regra do retângulo e pela regra do ponto médio
print("retangulo:", + rectangle_rule_sum,"ponto medio:", + midpoint_rule_sum)

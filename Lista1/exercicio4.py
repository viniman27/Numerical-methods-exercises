import math

# Ângulo em radianos
x = math.pi / 3

# Valor real de cos(pi/3)
cos_pi_3_real = math.cos(x)

# Cálculo da expansão de Taylor com três termos
termo_1 = 1  # O primeiro termo é sempre 1
termo_2 = -((x ** 2) / math.factorial(2))
termo_3 = ((x ** 4) / math.factorial(4))

# Valor aproximado usando os três termos
cos_pi_3_aproximado = termo_1 + termo_2 + termo_3

# Cálculo do erro de truncamento
erro_de_truncamento = cos_pi_3_real - cos_pi_3_aproximado

# Arredondamento para seis algarismos significativos
cos_pi_3_real = round(cos_pi_3_real, 6)
cos_pi_3_aproximado = round(cos_pi_3_aproximado, 6)
erro_de_truncamento = round(erro_de_truncamento, 6)

# Exibir os resultados
print(f'Valor real de cos(pi/3): {cos_pi_3_real}')
print(f'Valor aproximado com três termos da expansão de Taylor: {cos_pi_3_aproximado}')
print(f'Erro de truncamento: {erro_de_truncamento}')

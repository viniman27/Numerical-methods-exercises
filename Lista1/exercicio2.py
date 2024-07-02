import struct

# Número a ser representado
numero = 256.1875

# (a) Formato binário
parte_inteira_binario = bin(int(numero))[2:]

parte_fracionaria = numero - int(numero)
parte_fracionaria_binario = ''

while parte_fracionaria != 0:
    parte_fracionaria *= 2
    parte_fracionaria_binario += str(int(parte_fracionaria))
    parte_fracionaria -= int(parte_fracionaria)

numero_binario = parte_inteira_binario + '.' + parte_fracionaria_binario

# (b) Representação em ponto flutuante na base 2
representacao_ponto_flutuante = f'{numero:.8e}'

# (c) Cadeia de 64 bits em precisão dupla (IEEE-754)
numero_binario_precisao_dupla = struct.unpack('!Q', struct.pack('!d', numero))[0]
numero_binario_precisao_dupla = f'{numero_binario_precisao_dupla:064b}'

# Exibir os resultados
print(f'(a) Formato binário: {numero_binario}')
print(f'(b) Representação em ponto flutuante na base 2: {representacao_ponto_flutuante}')
print(f'(c) Cadeia de 64 bits em precisão dupla (IEEE-754): {numero_binario_precisao_dupla}')

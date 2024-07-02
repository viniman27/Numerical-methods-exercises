# Número binário
numero_binario = "11000101.101"

# Remova o ponto decimal para converter
numero_binario_sem_ponto = numero_binario.replace('.', '')

# Converta o número binário em decimal
numero_decimal = int(numero_binario_sem_ponto, 2)

print(f'O número binário {numero_binario} em decimal é: {numero_decimal}')

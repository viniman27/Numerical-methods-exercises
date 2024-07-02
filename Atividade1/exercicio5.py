def SIparaIng(cm, kg):
    # 1 centímetro = 0.393701 polegadas
    altura_polegadas = cm * 0.393701

    # 1 kg = 2.20462 libras
    peso_libras = kg * 2.20462

    return altura_polegadas, peso_libras

# Exemplo de uso da função
altura_cm = 178
massa_kg = 85
altura_polegadas, peso_libras = SIparaIng(altura_cm, massa_kg)

print(f"Altura em polegadas: {altura_polegadas:.2f} polegadas")
print(f"Peso em libras: {peso_libras:.2f} libras")

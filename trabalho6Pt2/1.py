# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Vinícius Assumpcção de Araújo - 200028472

import numpy as np

# Dados da tabela
# Raios em km (convertidos para metros multiplicando por 1000)
r_km = np.array([0, 800, 1200, 1400, 2000, 3000, 3400, 3600, 4000, 5000, 5500, 6370])
r = r_km * 1000  # Convertendo de km para m

# Densidades em kg/m^3
rho = np.array([13000, 12900, 12700, 12000, 11650, 10600, 9900, 5500, 5300, 4750, 4500, 3300])

# Constante pi
pi = np.pi

# Aplicar a regra trapezoidal
# A fórmula para a regra trapezoidal composta é:
# (b - a) * (f(a) + f(b) + 2 * sum(f(xi))) / (2n)
# Onde xi são os pontos intermediários entre a e b

# Cálculo da massa da Terra usando a regra trapezoidal composta
# m = ∫(ρ * 4 * π * r^2) dr de 0 a 6370km
# A função a ser integrada é ρ * 4 * π * r^2

# Calculamos a área de cada trapézio individual
trap_areas = np.zeros(r.shape[0] - 1)  # iniciamos um array de zeros para as áreas
for i in range(len(r) - 1):
    # A área do trapézio é dada pela média das alturas vezes a base
    avg_height = (rho[i] + rho[i + 1]) / 2
    base = r[i + 1] - r[i]
    trap_areas[i] = avg_height * base

# A função é ρ * 4 * π * r^2, então precisamos multiplicar as áreas por 4πr^2
# Fazemos isso para a média dos raios de cada trapézio
mass_segments = 4 * pi * ((r[:-1] + r[1:]) / 2) ** 2 * trap_areas

# A massa da Terra é a soma das massas de todos os segmentos
mass_earth = np.sum(mass_segments)

print(mass_earth)

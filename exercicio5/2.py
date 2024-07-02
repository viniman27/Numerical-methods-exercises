# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Vinícius Assumpcção de Araújo - 200028472


import numpy as np

# Dados
t = np.array([0, 25, 50, 75, 100, 125])  
y = np.array([0, 32, 58, 78, 92, 100])   

# Converter distancia para metros
y_meters = y * 1000

# Calculo usando diferenças finita

v_central = (y_meters[2:-1] - y_meters[0:-3]) / (t[2:-1] - t[0:-3])

# Primeiro ponto
v_forward = (y_meters[1] - y_meters[0]) / (t[1] - t[0])

# Ultimo ponto
v_backward = (y_meters[-1] - y_meters[-2]) / (t[-1] - t[-2])

# Combina os resultados em um vetor unico
velocities = np.concatenate(([v_forward], v_central, [v_backward])) / 1000

# Respostas
velocities_dict = {f"{t[i]}-{t[i+1]}s": velocities[i] for i in range(len(velocities))}
print("Velocidades: ",velocities_dict)

# Secao para calculo das aceleracoes

# Intervalos de tempo
t_midpoints = (t[1:-1] + t[0:-2]) / 2

# Velocities at midpoints for central differences (interpolating between the calculated velocities)
v_midpoints = (velocities[1:] + velocities[:-1]) / 2

# Calculo usando diferenças finita
a_central = (v_midpoints[1:] - v_midpoints[:-1]) / (t_midpoints[1:] - t_midpoints[:-1])

# Primeiro ponto
a_forward = (velocities[1] - velocities[0]) / (t_midpoints[0] - t[0])

# Ultimo ponto
a_backward = (velocities[-1] - velocities[-2]) / (t[-1] - t_midpoints[-1])

# Combina os resultados em um vetor unico
accelerations = np.concatenate(([a_forward], a_central, [a_backward]))

# Respostas
accelerations_dict = {f"{t[i]}-{t[i+1]}s": accelerations[i] for i in range(len(accelerations))}
print("Aceleracoes: ",accelerations_dict)

# Vinicius Assumpcao e Araujo - 200028472
#
#

import numpy as np

def load_data(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        data = [list(map(float, line.split())) for line in file]
    return np.array(data)

def linear_regression(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_xy = np.sum(x*y)
    
    a = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
    return a

filenames = ["DadosExp1.txt", "DadosExp2.txt", "DadosExp3.txt", "DadosExp4.txt", "DadosExp5.txt"]
slopes = []

for filename in filenames:
    data = load_data(filename)
    x, y = data[:, 0], data[:, 1]
    slope = linear_regression(x, y)
    slopes.append(slope)

average_slope = np.mean(slopes)
print(f"Módulo de Elasticidade (Inclinação Média): {average_slope} Pa")

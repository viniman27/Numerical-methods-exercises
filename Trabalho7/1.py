# Gabriel Roger Amorim da Cruz - 200018248
# Joáo Pedro de Camargo Vaz - 200020650
# Vinícius Assumpcção de Araújo - 200028472

import numpy as np
import matplotlib.pyplot as plt

# Dados fornecidos
m = 2.0  # massa em kg
k = 800.0  # constante da mola em N/m
F0 = 50.0  # amplitude da força de excitação em N
omega = 3.0  # frequência da força de excitação em rad/s
x0 = 0.1  # posição inicial em m
v0 = 0.1  # velocidade inicial em m/s
dt = 0.01  # passo de tempo em s
t_max = 10  # tempo máximo em s

# Funções para as derivadas da posição e da velocidade
def dxdt(t, x, v):
    """Calcula a derivada da posição."""
    return v

def dvdt(t, x, v):
    """Calcula a derivada da velocidade."""
    return (-k * x + F0 * np.cos(omega * t)) / m

# Array de tempo
t = np.arange(0, t_max + dt, dt)

# Condições iniciais
x = np.zeros_like(t)
v = np.zeros_like(t)
x[0] = x0
v[0] = v0

# Método de Euler
def euler_method(x, v, dt, t):
    """Implementa o método de Euler."""
    for i in range(1, len(t)):
        x[i] = x[i-1] + dxdt(t[i-1], x[i-1], v[i-1]) * dt
        v[i] = v[i-1] + dvdt(t[i-1], x[i-1], v[i-1]) * dt
    return x, v

# Método de Runge-Kutta de segunda ordem (Euler modificado)
def runge_kutta_2nd_order(x, v, dt, t):
    """Implementa o método de Runge-Kutta de segunda ordem."""
    for i in range(1, len(t)):
        k1_x = dxdt(t[i-1], x[i-1], v[i-1])
        k1_v = dvdt(t[i-1], x[i-1], v[i-1])

        k2_x = dxdt(t[i-1] + dt / 2, x[i-1] + k1_x * dt / 2, v[i-1] + k1_v * dt / 2)
        k2_v = dvdt(t[i-1] + dt / 2, x[i-1] + k1_x * dt / 2, v[i-1] + k1_v * dt / 2)

        x[i] = x[i-1] + k2_x * dt
        v[i] = v[i-1] + k2_v * dt
    return x, v

# Continuando o código do método de Runge-Kutta de quarta ordem
def runge_kutta_4th_order(x, v, dt, t):
    """Implementa o método de Runge-Kutta de quarta ordem."""
    for i in range(1, len(t)):
        k1_x = dxdt(t[i-1], x[i-1], v[i-1])
        k1_v = dvdt(t[i-1], x[i-1], v[i-1])

        k2_x = dxdt(t[i-1] + dt / 2, x[i-1] + k1_x * dt / 2, v[i-1] + k1_v * dt / 2)
        k2_v = dvdt(t[i-1] + dt / 2, x[i-1] + k1_x * dt / 2, v[i-1] + k1_v * dt / 2)

        k3_x = dxdt(t[i-1] + dt / 2, x[i-1] + k2_x * dt / 2, v[i-1] + k2_v * dt / 2)
        k3_v = dvdt(t[i-1] + dt / 2, x[i-1] + k2_x * dt / 2, v[i-1] + k2_v * dt / 2)

        k4_x = dxdt(t[i-1] + dt, x[i-1] + k3_x * dt, v[i-1] + k3_v * dt)
        k4_v = dvdt(t[i-1] + dt, x[i-1] + k3_x * dt, v[i-1] + k3_v * dt)

        x[i] = x[i-1] + (dt / 6) * (k1_x + 2*k2_x + 2*k3_x + k4_x)
        v[i] = v[i-1] + (dt / 6) * (k1_v + 2*k2_v + 2*k3_v + k4_v)
    return x, v

# Calcular a posição e a velocidade usando o método de Euler
x_euler, v_euler = euler_method(np.copy(x), np.copy(v), dt, t)

# Calcular a posição e a velocidade usando o método de Runge-Kutta de segunda ordem
x_rk2, v_rk2 = runge_kutta_2nd_order(np.copy(x), np.copy(v), dt, t)

# Calcular a posição e a velocidade usando o método de Runge-Kutta de quarta ordem
x_rk4, v_rk4 = runge_kutta_4th_order(np.copy(x), np.copy(v), dt, t)

# Agora vamos criar os gráficos para a posição (x) e a velocidade (v) em função do tempo (t)
# para cada um dos métodos numéricos utilizados.

# Plotando os resultados
plt.figure(figsize=(12, 10))

# Posição usando o método de Euler
plt.subplot(3, 2, 1)
plt.plot(t, x_euler, label='Euler')
plt.title('Posição (Euler)')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.grid()
plt.legend()

# Velocidade usando o método de Euler
plt.subplot(3, 2, 2)
plt.plot(t, v_euler, label='Euler')
plt.title('Velocidade (Euler)')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.grid()
plt.legend()

# Posição usando o método de Runge-Kutta de 2ª ordem
plt.subplot(3, 2, 3)
plt.plot(t, x_rk2, label='RK2')
plt.title('Posição (RK2)')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.grid()
plt.legend()

# Velocidade usando o método de Runge-Kutta de 2ª ordem
plt.subplot(3, 2, 4)
plt.plot(t, v_rk2, label='RK2')
plt.title('Velocidade (RK2)')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.grid()
plt.legend()

# Posição usando o método de Runge-Kutta de 4ª ordem
plt.subplot(3, 2, 5)
plt.plot(t, x_rk4, label='RK4')
plt.title('Posição (RK4)')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.grid()
plt.legend()

# Velocidade usando o método de Runge-Kutta de 4ª ordem
plt.subplot(3, 2, 6)
plt.plot(t, v_rk4, label='RK4')
plt.title('Velocidade (RK4)')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.grid()
plt.legend()


# Adjust layout
plt.tight_layout()
plt.show()
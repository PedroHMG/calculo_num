"""
Turma: T04 - MAT174
Componentes:
Ariel Pires
Marcelo Kenzo
Maria Laura
Pedro Henrique
Saulo Alves
Sohan Augustus
"""

import matplotlib.pyplot as plt
import numpy as np


# equação do deslocamento por tempo de uma vibração resonante
def f(t):
    y = (0.05 - (t / 20)) * np.cos(10 * t) + ((1 / 200) * np.sin(10 * t))
    return y


# Deslocamento que queremos encontrar para o problema
d_max = 0.065

# Lista com a relação x com y. x de 0 a t_max e com "steps" de e1
e1 = 0.05
t_max = 5
t_list = np.arange(0, t_max, e1)
y_list = f(t_list)

# Plotagem do grafico
fig, axs = plt.subplots(1, 2, figsize=(15, 5))
fig.suptitle('Gráfico do Tempo x Amplitude')
axs[0].plot(t_list, y_list)
axs[0].axis([0, t_max, -d_max * 1.8, d_max * 1.8])
axs[0].grid(True)
axs[0].set(xlabel='t(s)', ylabel='A(m)')

# linhas pontilhadas y = +- d_max
axs[0].axhline(y=-d_max, color='g', linestyle='--')
axs[0].axhline(y=d_max, color='r', linestyle='--')

# Plotagem aproximada do grafico da primeira intersecção com a equação da amplitude
axs[1].plot(t_list, y_list)
axs[1].axis([2, 3, -d_max * 1.8, d_max * 1.8])
axs[1].axhline(y=-d_max, color='g', linestyle='--')
axs[1].grid(True)
axs[1].set(xlabel='t(s)', ylabel='A(m)')

# Faz aparecer o gráfico
plt.show()

# A linha y = - d_max será o novo y = 0
y_list -= d_max

# identificação dos itervalos usando o teorema de Bolzano
for index in range(len(y_list)):
    if y_list[index] * y_list[index + 1] < 0:
        x0, x1 = [t_list[index], t_list[index + 1]]
        print(f'Para y = {-d_max}; o intervalo será: ', x0, x1)
        break

# A linha y = + d_max será o novo y = 0
y_list += 2 * d_max
for index in range(len(y_list)):
    if y_list[index] * y_list[index + 1] < 0:
        x0, x1 = [t_list[index], t_list[index + 1]]
        print(f'Para y = {d_max}; o intervalo será: ', x0, x1)
        break

# O intervalo da linha y = + d_max é mais próximo que y = - d_max

# Distância mínima esperada para e
e = 0.0000001
times = 0

# Método da bissecção
'''
while e < e1:
    times += 1
    q = ((x0+x1)/2)
    if (f(x0) + d_max) * (f(q) + d_max) < 0:
        x1 = q
    else:
        x0 = q
    e1 = x1 - x0
    print(e1)
    print(x0, x1)
'''

# Utilização do método da secante verificando a distância entre os x
while e < e1:
    times += 1
    # Secante
    q = ((f(x0 + e1) - f(x0)) / e1)
    # Novo valor para x utilizando a secante descoberta anteriormente
    x1 = x0 - ((f(x0) + d_max) / q)
    # calculo da distância de entre o x anterior e o encontrado
    e1 = abs(x1 - x0)
    print('valor de e:', e1)
    x0 = x1
    print('valor de x:', x0)

print('Result:', x0, 'seconds')


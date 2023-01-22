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

import numpy as np
import matplotlib.pyplot as plt


def f(x, raio):
    y = np.sqrt(np.power(raio, 2) - np.power(x, 2))
    return y


def qx(x, y):
    q = 0
    for index in range(len(x) - 1):
        # base do elemento
        b = x[index + 1] - x[index]

        # verifica qual altura é a menor
        if y[index] < y[index + 1]:
            h_rect = y[index]
        else:
            h_rect = y[index + 1]

        # base vezes altura vezes a metade da altura (b * h^2)/2
        q += b * np.power(h_rect, 2) / 2

        # qx para o triângulo (b * h) / 2 * (h/3 + b_rect)
        h_tri = abs(y[index] - y[index + 1])
        q += b * h_tri / 2 * (h_tri / 3 + h_rect)
    return q


# calcular a área
def area(x, y):
    a = 0
    for index in range(len(x) - 1):
        # base
        b = x[index + 1] - x[index]
        a += b * (y[index] + y[index + 1]) / 2
    return a


def second_moment(x, y, y_line):
    i = 0
    for index in range(len(x) - 1):
        # base do elemento
        b = x[index + 1] - x[index]

        # verifica qual altura é a menor
        if y[index] < y[index + 1]:
            h_rect = y[index]
        else:
            h_rect = y[index + 1]

        # (b * h^3)/12 + A*y - Retângulo
        i += (b * np.power(h_rect, 3) / 12) + (b * h_rect * (np.power(h_rect / 2 - y_line, 2)))

        # (A * h^2)/6 + A*y - Triangulo
        h_tri = abs(y[index] - y[index + 1])
        a_tri = b * h_tri / 2
        i += (a_tri * np.power(h_tri, 2) / 6) + (a_tri * np.power(h_tri / 3 + h_rect - y_line, 2))
    return i


# Momento fletor
V = 2 * 10 ** 6

# raio
r = 50

# variável que controla as subdivisões
n = 1 / 50 * 50
x_list = np.arange((-r + 10) * n, ((r - 10) * n) + 1) / n
y_list = f(x_list, r)

print(x_list)
print(y_list)
print('Qx: ', qx(x_list, y_list))
print("Área: ", area(x_list, y_list))

# y médio
y_ = qx(x_list, y_list) / area(x_list, y_list)
print('y médio: ', y_)

Iz = second_moment(x_list, y_list, y_)
print("Segundo momento: ", Iz)

# Cálculo da tensão normal
normal_stress = V * (r - y_) / Iz
print("Tensão normal: ", normal_stress)
print('número de subdivisões:', len(x_list) - 1)
print('Erro relativo - CAE: ', (normal_stress - 87.866) / 87.866 * 100, '%')

# Cálculo do erro estimado
f2max = 0.0925925925926
erro_est = abs(np.power((r - 10) * 2, 3) / (12 * np.power(len(x_list), 2)) * f2max)
print('Erro estimado: ', erro_est)

# plotar o gráfico
fig, axes = plt.subplots(figsize=(10, 5))
axes.set_ylim([-5, 55])
plt.plot(x_list, y_list, 'b')
plt.plot([x_list[0], x_list[0]], [y_list[0], 0], 'b')
plt.plot([x_list[-1], x_list[-1]], [y_list[-1], 0], 'b')
plt.plot([x_list[0], x_list[-1]], [0, 0], 'b')
plt.show()


import numpy as np
import matplotlib.pyplot as plt

'''
n = int(input('Digite quantos pontos são: '))
x = []
y = []
m = 0
for m in range(0, n):
    k = float(input('Digite o valor de x' + str(m) + ': '))
    x.append(k)
    k = float(input('Digite o valor de y' + str(m) + ': '))
    y.append(k)
'''



def interpNewton(x, y, xi):
    n = len(x)
    fdd = np.zeros((n, n))
    yint = [0 for x in range(n)]
    yint2 = [0 for x in range(n)]

    for i in range(n):
        fdd[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            fdd[i][j] = (fdd[i + 1][j - 1] - fdd[i][j - 1]) / (x[i + j] - x[i])
    xterm = 1
    yint = fdd[0][0]
    yint2 = fdd[0][0]
    for order in range(1, n - 1):
        xterm = xterm * (xi - x[order - 1])
        yint = yint + fdd[0][order] * xterm
    xterm = 1
    for order in range(1, n):
        xterm = xterm * (xi - x[order - 1])
        yint2 = yint2 + fdd[0][order] * xterm
    return [yint, fdd, yint2]


small_data_x = [0.015, 0.04, 0.07]
small_data_y = [1520, 1906, 2042]
n = len(small_data_y)

print(small_data_x)
print(small_data_y)
xp = float(input('Digite um valor dentro do intervalo de ' + str(small_data_x[0]) + ' a ' + str(small_data_x[n - 2]) + ': '))
yp, fdd, d = interpNewton(small_data_x, small_data_y, xp)
t = np.arange(small_data_x[0] - 0.1, 0.1 + small_data_x[2], 0.1)
yt = []
yt2 = []
for i in t:
    yt.append(interpNewton(small_data_x, small_data_y, i)[0])
for i in t:
    yt2.append(interpNewton(small_data_x, small_data_y, i)[2])
plt.plot(t, yt, 'b-')
plt.plot(t, yt2, 'y-')
plt.plot(small_data_x, small_data_y, 'ro')
plt.plot(xp, yp, 'g*')
plt.legend(['Polinomio de grau ' + str(n - 2), 'Polinomio de grau ' + str(n - 1), 'Ponto vermelho', 'Ponto verde'],
           loc=1)
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.title('Interpolação de Newton')
plt.show()
print('g(%.3f) = %.3f' % (xp, yp))
error = 1
for g in range(n):
    error = error * abs(xp - small_data_x[g])
error = error * abs(fdd[0, n - 1])
print(error)

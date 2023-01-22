n = len(small_data_x)


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


index_list = []
num = 0.11
for index in range(len(data_x) - 1):
    if data_x[index] < num < data_x[index + 1]:
        inter = [index, index + 1]
        if not (data_x[index + 1] and data_x[index + 2]) == data_x[-1]:
            for item in range(3):
                index_list.append(index + item)
        else:
            for item in range(3):
                index_list.append(index + 1 - item)

            index_list = np.flip(index_list)
        break

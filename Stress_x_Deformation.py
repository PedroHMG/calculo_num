import numpy as np
import matplotlib.pyplot as plt

raw_data = '''
0	0.0000000
323	0.0010039
970	0.0029921
1134 0.0039961
1180 0.0050000
1305 0.0075000
1373 0.0100000
1520 0.0150000
1906 0.0400000
2042 0.0700000
2031 0.0800000
1929 0.1000000
1588 0.1150000
'''
raw_data = raw_data.replace('\n', ' ').split()

data_x = []
data_y = []
for y, x in zip(raw_data[::2], raw_data[1::2]):
    data_x.append(float(x))
    data_y.append(int(y))

data_x = np.array(data_x)
data_y = np.array(data_y)

plt.plot(data_x, data_y)
plt.show()

num = float(input(f"Insira a deformação desejada entre {data_x[0]} e {data_x[-1]}: "))
if data_x[0] > num or num > data_x[-1]:
    print("Número maior que o intervalo!")
    exit()

'''
n = 5
elastic_x = []
elastic_y = data_y[:n]

for x in data_x[:n]:
    elastic_x.append(x + 0.002)

print(elastic_y)
print(elastic_x)
'''


def divided_diff(x, y):
    n = len(y)
    ordem = np.zeros([n, n])
    ordem[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            ordem[i][j] = (ordem[i + 1][j - 1] - ordem[i][j - 1]) / (x[i + j] - x[i])
    return ordem


def find_y(num, data_x, list_a):
    x_subt = num - np.array(data_x)
    y_result = list_a[0, 0]
    count = 1
    for a in list_a[0, 1:]:
        y_result += a * np.prod(x_subt[:count])
        count += 1
    return y_result


def error(num, data_x, list_a, matrix_a):
    max_fx = abs(matrix_a[:, len(data_x)]).max()
    x_subt = num - np.array(data_x)

    erro = abs(np.prod(x_subt) * max_fx)
    return erro


index_list = []
for index in range(len(data_x) - 1):
    if data_x[index] < num < data_x[index + 1]:
        inter = [index, index + 1]
        if not data_x[index + 1] == data_x[-1]:
            for item in range(3):
                index_list.append(index + item)
        else:
            for item in range(3):
                index_list.append(index + 1 - item)

            index_list = np.flip(index_list)
        break


a_matrix = divided_diff(data_x, data_y)
a_list = a_matrix[index_list, : len(index_list)]


x_test = np.arange(data_x[index_list[0]] - 0.005, data_x[index_list[-1]] + 0.005, 0.0001)
y_test = []
for item in x_test:
    y_test.append(find_y(item, data_x[index_list], a_list))

calc_error = error(num, data_x[index_list], a_list, a_matrix)

stress = find_y(num, data_x[index_list], a_list)
print("tensão: ", find_y(num, data_x[index_list], a_list), "KPa")
print("erro de interpolação: ", calc_error)

#######################################################################

n = 3
ax = plt.gca()
plt.legend(['Polinomio de grau ' + str(n - 2), 'Polinomio de grau ' + str(n - 1), 'Ponto vermelho', 'Ponto verde'],
           loc=1)
plt.title('Interpolação de Newton')

plt.xlabel('Deformação (mm/mm)')
plt.ylabel('Tensão (KPa)')


ax.text(num, stress, int(stress), size=10)
plt.grid()
ax.set_ylim(data_y[index_list].min() * 0.9, data_y[index_list].max() * 1.1)
ax.set_xlim(data_x[index_list].min() * 0.9, data_x[index_list].max() * 1.1)
plt.plot([num], [stress], 'g*')
plt.scatter(data_x[index_list], data_y[index_list])
plt.plot(x_test, y_test)
plt.plot(data_x[inter], data_y[inter], 'g')
plt.show()

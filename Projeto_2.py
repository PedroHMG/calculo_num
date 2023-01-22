import numpy as np

A = 100
E = 70000


#  matriz de rigidez do elemento
def stiff_matrix(x, y, a=100):
    l = np.sqrt(x**2 + y**2)
    matrix = np.array([[x ** 2, x * y, -x ** 2, -x * y],
                       [x * y, y ** 2, -x * y, -y ** 2],
                       [-x ** 2, -x * y, x ** 2, x * y],
                       [-x * y, -y ** 2, x * y, y ** 2]])
    return (E * a / (l ** 3)) * matrix


# soma na matriz de rigidez geral
def add_to_kt(k, i, j):
    num_rows = np.shape(k)[0]
    # j = 2 * j
    # i = 2 * i - 1

    degree_free = [(2 * i - 2), (2 * i - 1), (2 * j - 2), (2 * j - 1)]
    for i, r in zip(degree_free, range(num_rows)):
        for j, t in zip(degree_free, range(num_rows)):
            kt[i][j] += k[r][t]
    return kt


k1 = stiff_matrix(0, 500)
k2 = stiff_matrix(500, 0)
k3 = stiff_matrix(500, -500)

# Definimos o vetor força e vetor grau de liberdade dos nós
force = np.array(['r', 'r', 1000, 0, 0, 'r'])
u = np.array([0, 0, 1, 1, 1, 0])

row_columns = np.shape(force)[0]

# Matriz geral de rigidez:
kt = np.zeros([row_columns, row_columns])
icog = []
for x in range(1, row_columns + 1):
    icog.append(f'u{x}')

# somar na matriz de rigidez
add_to_kt(k1, 1, 2)
add_to_kt(k2, 1, 3)
add_to_kt(k3, 2, 3)

np.set_printoptions(precision=10)

# salvar as colunas e linhas que serão deletadas
delete = []
for item, q in zip(force, range(row_columns)):
    if item == 'r':
        delete.append(q)

kt_u_trim = kt * u
force = np.where(force == 'r', 0, force).astype(np.int32)

# Deletando linhas e colunas
force = np.delete(force, delete, 0)
icog = np.delete(icog, delete, 0)
kt_u_trim = np.delete(kt_u_trim, delete, 0)
kt_u_trim = np.delete(kt_u_trim, delete, 1)


print(kt_u_trim)
print(force)


L = np.tril(kt_u_trim)
U = kt_u_trim - L

x1 = np.array([0, 0, 0])
e = 0.0000001
e1 = e2 = e3 = 10 * e

while e < e1 and e < e2 and e < e3:
    x = np.linalg.inv(L).dot((force - U.dot(x1)))
    e1, e2, e3 = abs(x - x1)
    x1 = x

print('Deslocamento nó 2: ', np.sqrt(np.square(x[0])+np.square(x[1])))
print('Deslocamento nó 3: ', x[2])

for x, y in zip(icog, x):
    print(f'{x}:', y)



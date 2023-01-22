import numpy as np

A = np.array([[4949.74746831, -4949.74746831, -4949.74746831],
              [-4949.74746831, 18949.74746831,  4949.74746831],
              [-4949.74746831,  4949.74746831, 18949.74746831]])
b = np.array([1000, 0, 0])
x1 = np.array([0, 0, 0])

L = np.tril(A)
U = A - L

e = 0.0000001
e1 = e2 = e3 = 10 * e

while e < e1 and e < e2 and e < e3:
    x = np.linalg.inv(L).dot((b - U.dot(x1)))
    e1, e2, e3 = abs(x - x1)
    x1 = x


print(L)
print(U)
print(x)
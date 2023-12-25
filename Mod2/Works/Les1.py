import numpy as np 

a = [3, 5]
b = [4, 1]
print(a*2)

a = np.array([3, 5])
b = np.array([4, 1])
print(a*2)

a = np.array([1, 2, 6, 3, 87, -6])
print(a.sum())
print(a.max())
print(a.min())
print(a.argsort())

a = np.array([1, 2, 3])
b = np.array([1, 0, 1])
print(a * b)
print(a ** b)
print(a @ b)

a = np.array([1, 5, 3, 8 , -4, 8, 2])
print(a > 1)
print((a > 1).sum())
print(a.mean())
print(a.std)
print(a.cumsum)
print(np.full(5, 7))
print(np.linspace(2, 3, 5))
print(np.logspace(1, 3, 3, base=2))
print(np.ones(40))
print(np.zeros(40))
print(np.sin(np.pi /2))
print(np.arange(1, 10, 3))


b = np.array([1, 0, 1])
print(np.cos([np.pi, 0]))
##Матрицы

A = np.array([[10, 7, 8], [9, 8, 9]])
print(A)
print(A.shape)
print(A.size)
print(A[1, 2])
print(A[1])
print(A[:, 1])
B = np.array([[1, 4], [9, 3], [0, -6]])
print(B)

print(B.ravel())
B.shape = 2, 3
print(B)

a = np.array([3, 6, 2, 4, 7])
print((a % 2 == 0).sum())

print((a % 2 != 0).mean())


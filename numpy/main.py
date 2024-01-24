import numpy as np
# import matplotlib.pyplot as plt

# A numpy is a library used for scientific computation

a = np.array([0, 1, 2, 3, 4])
print(a[1:])
# Checking numpy version
print(np.__version__)
# Checking array type
print(type(a))
print(a.dtype)
print(a[1:4])
print(a.ndim)
print(a.size)
print(a.shape)
# Get the mean
mean = a.mean()
print(mean)
# Standard deviation
std = a.std()
print(std)
# biggest value you use max, smallest, min

# Adding two arrays
u = np.array([1, 3, 4])
v = np.array([2, 2, 3])
z = np.add(u, v)
print(z)
# Subtracting two arrays
z = np.subtract(u, v)
print(z)
# Multiplying
z = np.multiply(u, v)
print(z)
# Divide
z = np.divide(u, v)
print(z)
# Dot multiplication
z = np.dot(u, v)
print(z)
# Adding a constant to an array
print(v + 3)

# Math fxns
x = np.array([0, np.pi/2, np.pi])
print(x)
y = np.sin(x)
print(y)

# Line spacing
t = np.linspace(-2, 2, num=9)
r = np.linspace(0, 2*np.pi, num=100)
print(t)
print(r)
w = np.sin(r)
# plt.plot(r, w)

# 2 Dimensional Array
A = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])
Z = np.dot(A, B)
print(Z)
C = np.array([[0, 1, 1], [1, 0, 1]])
D = np.array([[1, 1, 3], [1, 1, 2], [-1, 1, 4]])
Y = np.dot(C, D)
print(Y)
print(Y.ndim)
# For transpose
L = Y.T
print(L)

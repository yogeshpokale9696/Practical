import numpy as np

a1 = np.zeros((2, 2))
print(a1, "\n")

b = np.ones((1, 2))
print(b, "\n")

c = np.full((2, 2), 7)
print(c, "\n")

d = np.eye(2)
print(d, "\n")

e = np.random.random((2, 2))
print(e, "\n")

# Array Slicing syntax  array=[start:end:step]
print("Array Slicing")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2], "\n")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr)
print(arr[1, 1:4], "\n")  # first tuppel 1 to 4 element 4 not included

print(arr[0:2, 2], "\n")  # print particular element at 2 of 0 to 2 th tuppel
print(arr[0:2, 1:4], "\n")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr, "\n")
row_r1 = arr[1, :]
print(row_r1, "\n")
print(row_r1.shape)

row_r2 = arr[:2, 1:3]
print(row_r2, "\n")
print(row_r2.shape, "\n")

row_r3 = arr[1:3, 1:3]
print(row_r3, "\n")
print(row_r3.shape, "\n")

row_r4 = arr[1:2, :]
print(row_r4, "\n")
print(row_r4.shape, "\n")

# printing columns

print(arr, "\nColumns")

print(arr[:, 1])

# Arrange
print("\nArrange\n")

a = np.array([[1, 2, 3], [3, 2, 4], [7, 8, 9], [10, 11, 12]])
print(a, "\n\n")
b = np.array([0, 2, 1, 0])
print(a[np.arange(4), b], "\n")  # print a array according to b array as position

# array math
print("Array Math\n")

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
print(np.add(x, y), "\n")

print(np.subtract(x, y), "\n")

print(np.multiply(x, y), "\n")

print(np.divide(x, y), "\n")

print(np.sqrt(x), "\n")

x = np.array([3, 5])
y = np.array([2, 5])

print("Greater", np.greater(x, y), "\n")

x = np.array([[1, 2], [3, 4]])
print(np.sum(x), "\n")
print(np.sum(x, axis=0), "\n")
print(np.sum(x, axis=1), "\n")

# transpose
print("Transpose")

x = np.array([[1, 2], [3, 4]])
print(x, "\n")
print(x.T, "\n")

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 8])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
print(np.intersect1d(a, b), "\n")

import numpy as np

# Generate two 3x3 matrices with random integers from 1 to 9
matrix1 = np.random.randint(1, 10, (3, 3))
matrix2 = np.random.randint(1, 10, (3, 3))

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Matrix Addition
addition = matrix1 + matrix2

# Matrix Multiplication
multiplication = np.dot(matrix1, matrix2)

print("\nMatrix Addition:")
print(addition)

print("\nMatrix Multiplication:")
print(multiplication)
import numpy as np

# Creating Arrays
array_1d = np.array([1, 2, 3, 4])
array_2d = np.array([[1, 2], [3, 4]])

# Mathematical Operations
sum_array = array_1d + 10  # Broadcasting
product_array = array_1d * 2
dot_product = np.dot(array_2d, array_2d)

print("Original Array:", array_1d)
print("Array + 10:", sum_array)
print("Array * 2:", product_array)
print("Dot Product of 2D Array:\n", dot_product)

# Statistical Operations
print("Mean:", np.mean(array_1d))
print("Standard Deviation:", np.std(array_1d))
print("Sum of All Elements:", np.sum(array_2d))

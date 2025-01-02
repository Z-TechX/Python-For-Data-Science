import numpy as np
# Indexing and Slicing
array = np.array([10, 20, 30, 40, 50])
print("Element at Index 2:", array[2])
print("Slice (1:4):", array[1:4])

# Reshaping
array_reshaped = np.arange(1, 10).reshape(3, 3)
print("Reshaped Array:\n", array_reshaped)

# Flattening
flattened = array_reshaped.flatten()
print("Flattened Array:", flattened)

# Boolean Indexing
mask = array > 30
print("Elements Greater Than 30:", array[mask])

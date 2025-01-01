# ---------------------- LIST COMPREHENSIONS ----------------------

# Using a loop to create a list of squares
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print("Squares using loop:", squares)

# List comprehension to create a list of squares
squares_comp = [i ** 2 for i in range(1, 6)]
print("Squares using list comprehension:", squares_comp)

# Filtering even numbers using list comprehension
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print("Even numbers using list comprehension:", even_numbers)

# ---------------------- SLICING ----------------------

# Creating a list
numbers = [10, 20, 30, 40, 50]

# Slicing a list
print("First three elements:", numbers[:3])  # First three items
print("Last two elements:", numbers[-2:])   # Last two items
print("Middle elements:", numbers[1:4])     # Middle items from index 1 to 3

# Slicing with step (every second element)
print("Every second element:", numbers[::2])

# Reversing the list using slicing
print("Reversed list using slicing:", numbers[::-1])

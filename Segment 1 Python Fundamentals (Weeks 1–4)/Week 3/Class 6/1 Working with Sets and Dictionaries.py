# ---------------------- SETS ----------------------

# Creating a set
unique_numbers = {1, 2, 3, 4, 5}
print("Original Set:", unique_numbers)

# Adding an item to the set
unique_numbers.add(6)
print("After adding 6:", unique_numbers)

# Removing an item from the set
unique_numbers.remove(3)  # Raises KeyError if item is not found
print("After removing 3:", unique_numbers)

# Discarding an item from the set (does not raise error if item is not found)
unique_numbers.discard(10)  # Item doesn't exist, no error
print("After discarding 10 (non-existent item):", unique_numbers)

# Checking membership in a set
if 2 in unique_numbers:
    print("2 is in the set.")

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union of set_a and set_b:", set_a | set_b)        # Union
print("Intersection of set_a and set_b:", set_a & set_b)  # Intersection
print("Difference of set_a and set_b:", set_a - set_b)    # Difference

# ---------------------- DICTIONARIES ----------------------

# Creating a dictionary
student = {"name": "Alice", "age": 20, "grade": "A"}
print("Original Dictionary:", student)

# Accessing values in a dictionary
print("Name:", student["name"])

# Adding a new key-value pair
student["school"] = "Greenwood High"
print("After adding school:", student)

# Updating an existing value
student["grade"] = "A+"
print("After updating grade:", student)

# Removing a key-value pair using pop()
removed_value = student.pop("age")
print("Removed value from 'age':", removed_value)
print("After removing 'age':", student)

# Removing a key-value pair using del
del student["grade"]
print("After deleting 'grade':", student)

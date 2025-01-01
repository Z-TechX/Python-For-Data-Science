# ---------------------- LISTS ----------------------

# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)

# Accessing items in a list
print("First item in list:", fruits[0])

# Adding an item to the list
fruits.append("orange")
print("After appending 'orange':", fruits)

# Inserting an item at a specific position
fruits.insert(1, "grape")
print("After inserting 'grape' at index 1:", fruits)

# Removing an item by value
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Removing an item by index
removed_item = fruits.pop(2)
print("After popping index 2 (removed item was: ", removed_item, "):", fruits)

# Reversing the list
fruits.reverse()
print("After reversing the list:", fruits)

# Sorting the list
fruits.sort()
print("After sorting the list:", fruits)

# ---------------------- TUPLES ----------------------

# Creating a tuple
numbers = (1, 2, 3, 4)
print("Original Tuple:", numbers)

# Accessing items in a tuple
print("First item in tuple:", numbers[0])

# Checking if an item exists in a tuple
if 3 in numbers:
    print("3 is in the tuple.")

# Slicing a tuple
print("Sliced Tuple (first 2 elements):", numbers[:2])

# Tuples are immutable, so we can't directly change them.
# We convert the tuple to a list to modify it.
numbers_list = list(numbers)
numbers_list.append(5)
numbers = tuple(numbers_list)
print("After appending 5 (converted back to tuple):", numbers)

# ---------------------- DICTIONARY METHODS ----------------------

# Creating a dictionary
student = {"name": "Bob", "age": 18, "grade": "B"}
print("Original Dictionary:", student)

# Accessing keys, values, and items
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Using get method to retrieve a value (returns None if key doesn't exist)
print("Grade using get:", student.get("grade"))
print("Address using get:", student.get("address"))  # Non-existent key

# Using setdefault() to get the value or set a default if key doesn't exist
print("Address using setdefault:", student.setdefault("address", "Unknown"))

# ---------------------- ADDING/REMOVING KEY-VALUE PAIRS ----------------------

# Adding a key-value pair
student["email"] = "bob@example.com"
print("After adding email:", student)

# Removing a key-value pair using pop()
removed_value = student.pop("email")
print("After popping 'email', removed value:", removed_value)
print("Dictionary after pop:", student)

# Using del to delete a key-value pair
del student["age"]
print("After deleting 'age':", student)

# Clearing the entire dictionary
student.clear()
print("After clearing the dictionary:", student)

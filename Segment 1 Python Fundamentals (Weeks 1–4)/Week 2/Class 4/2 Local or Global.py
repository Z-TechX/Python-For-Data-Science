# Global variable
total = 0

def add_to_total(amount):
    # Local variable
    total = 5  # This total is different from the global one
    print(f"Inside the function, local total is: {total}")
    global_total = globals()['total']  # Accessing the global variable
    globals()['total'] = global_total + amount  # Modifying the global variable

# Display initial global total
print(f"Initial global total: {total}")

# Call the function
add_to_total(10)

# Display updated global total
print(f"After calling the function, global total is: {total}")

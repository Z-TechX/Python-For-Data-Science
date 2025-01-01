try:
    # Attempting to read a non-existent file
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
finally:
    print("Execution of the try-except-finally block is complete.")

try:
    # Attempting to divide by zero
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
finally:
    print("This block runs no matter what.")

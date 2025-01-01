# Creating and writing to a file
with open("intro.txt", "w") as file:
    file.write("Welcome to the introduction of file handling in Python.\n")

# Reading from the file
with open("intro.txt", "r") as file:
    content = file.read()
    print("File content after writing:")
    print(content)

# Appending to the file
with open("intro.txt", "a") as file:
    file.write("Let's learn how to append data.")

# Reading the updated file
with open("intro.txt", "r") as file:
    content = file.read()
    print("\nFile content after appending:")
    print(content)

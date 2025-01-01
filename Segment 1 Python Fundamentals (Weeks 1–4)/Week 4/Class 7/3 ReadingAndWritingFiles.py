# Writing to a text file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("This is the second line.")

# Reading from the text file
with open("sample.txt", "r") as file:
    content = file.read()
    print("Content of text file:")
    print(content)

# Writing to a CSV file
import csv

with open("sample.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "San Francisco"])

# Reading from the CSV file
with open("sample.csv", "r") as file:
    reader = csv.reader(file)
    print("\nContent of CSV file:")
    for row in reader:
        print(row)

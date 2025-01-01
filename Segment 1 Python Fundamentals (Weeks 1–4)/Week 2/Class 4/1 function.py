# Function to calculate the square of a number
def calculate_square(number):  #return type function with parameter
    # Calculate the square
    result = number * number
    return result  # Return the result to the caller

def calculate_square_root(): #non return type function with no parameter
    num1 = int(input("Enter a square number to find its root: "))
    print(f"The root if {num1} is {num1**(1/2)}")
    #no return. Print is needed so that we can see the result

# Input from the user
num = int(input("Enter a number to find its square: "))

# Call the function and store the result
square = calculate_square(num)

# Display the result
print(f"The square of {num} is {square}.")
calculate_square_root() #Function calling

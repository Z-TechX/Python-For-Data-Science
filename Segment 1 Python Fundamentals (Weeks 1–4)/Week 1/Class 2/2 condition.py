num1 = input("Enter first number: ")
num2 = input("Enter second number: ")


if num1>num2: #IF statement is the condition and this is checked at first 
    print("Number 1 is greater than Number 2") #the indent (space) is most important also dont mix space and tab
elif num1<num2: #elif is else if and this will be checked if the IF statement is FALSE
    print("Number 2 is greater than Number 1")
else: #ELSE will run if IF statement and all ELIF statements are false. ELSE is TRUE if all others are FALSE
    print("They are equal")


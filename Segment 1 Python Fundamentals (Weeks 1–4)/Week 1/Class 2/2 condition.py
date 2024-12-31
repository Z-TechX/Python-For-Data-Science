num1 = input("Enter first number: ")
num2 = input("Enter second number: ")


if num1>num2: #IF statement is the condition and this is checked at first 
    print("Number 1 is greater than Number 2") #the indent (space) is most important also dont mix space and tab
elif num1<num2: #elif is else if and this will be checked if the IF statement is FALSE
    print("Number 2 is greater than Number 1")
else: #ELSE will run if IF statement and all ELIF statements are false. ELSE is TRUE if all others are FALSE
    print("They are equal")



# match num1:           #python version 3.10 or newer only
#     case "10":    
#          print("10") #this will print if and only if the case is true
#     case "20":
#          print("20")
#     case "30":
#          print("30")
#     case _:
#         print("Default") #this will print if no case is true
# Lets make a For Ever Loop and using operators in condition to make a small calculator
# Take 2 numbers as input. Remember to convert them to Floats (Floats as we will devide also)
# We will take another variable for operators 

#Hint
num1,num2 = 1,2 #take as user input
operator = input("input operator: ")

if operator == "+":
    result = num1+num2
elif operator == "-":
    result = num1-num2
#... and so on

#remember to check if num2 == 0 you can not devide

print(num1,operator,num2,"=",result)
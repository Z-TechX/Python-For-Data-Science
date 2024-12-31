#Take a studnet's grade into input in variable "Grade". Convert the string to int using int().
#The input can not be greater than 100 or less then 0.
#Check and print which Letter Grade the student got.

# Grade Points are
# 90 - 100 = A
# 80 - 89 = B
# 70 - 79 = C
# 60 - 69 = D
# 50 - 59 = E
#  0 - 49 = F



#hint
grade = input("......") #write your message
#convert to int

Letter = ""

#condition
if grade >0 or grade < 100:  #within the bound
    if grade >= 90 and grade <= 100:
        Letter = "A" #keeping the output in a varibale
    elif grade >= 80 and grade < 90:
        Letter = "B"
        #...... and so on


else:
    print("invalid")

print("The Student got:",Letter) #printing the last output
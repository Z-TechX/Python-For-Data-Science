var1 = input("Input a number: ") #input always makes the variable type STR or String.
print("Type of var1 is :",type(var1),"value of var1 is",var1)

#we need to convert the input to int or float to do oreration on them like:

var2 = int(var1) #string to int
print("Type of var2 is :",type(var2),"value of var2 is",var2)

var3 = float(var1) #string to float
print("Type of var3 is :",type(var3),"value of var3 is",var3)

var4 = float(var2) #int to float
print("Type of var4 is :",type(var4),"value of var4 is",var4)

var5 = str(var2) #int to string
print("Type of var5 is :",type(var5),"value of var5 is",var5)

var6 = str(var3) #float to string
print("Type of var6 is :",type(var6),"value of var6 is",var6)

var7 = int(var3) #float to int
print("Type of var7 is :",type(var7),"value of var7 is",var7)


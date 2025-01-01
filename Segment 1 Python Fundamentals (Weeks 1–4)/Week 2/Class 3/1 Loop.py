# Demonstration of Loops in Python

# FOR LOOP: Counting numbers
print("For Loop Example:")
for i in range(1, 6):  # Loop from 1 to 5
    print("Counting:", i)
print()

# WHILE LOOP: Counting down
print("While Loop Example:")
x = 5
while x > 0:  # Loop until x becomes 0
    print("Counting down:", x)
    x -= 1  # Decrease x by 1
print()

# BREAK: Stop the loop when a condition is met
print("Using Break in a Loop:")
y = 1
while True:  # Infinite loop
    print("Number:", y)
    if y == 3:  # Stop when y equals 3
        print("Breaking the loop.")
        break
    y += 1
print()

# CONTINUE: Skip a specific condition
print("Using Continue in a Loop:")
for i in range(1, 6):  # Loop from 1 to 5
    if i == 3:  # Skip the number 3
        continue
    print("Number:", i)
print()

# ELSE WITH LOOPS: Verify a condition was not met
print("Using Else with a Loop:")
num = 1
while num <= 3:
    if num == 4:  # This will never happen
        break
    print("Checking:", num)
    num += 1
else:
    print("The loop completed without breaking.")
print()

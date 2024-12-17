# Program to calculate the average of even numbers in a list
numbers = [1, 2, 3, 4, 5, 6]
total = 0
count = 0
# Syntax Error: 
for num in numbers
    if num % 2 == 0:  
        total += num
        count += 1
# Logical Error: 
if count == 0: 
    average = total 
else:
    average = total  
print("The average of even numbers is:", average)
# Logical Error: 
if average > 0:
    print("Average is positive!")
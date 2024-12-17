# Program to calculate factorial
def factorial(num)
    if num < 0:  
        return "Error! Factorial does not exist for negative numbers."
    elif num == 0
        return 1
    else
        result = 1
        for i in range(1, num + 1): 
        result = result * i  
    return result

n = input("Enter a number: ")  
print("The factorial of", n, "is", factorial(n))  

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument
number = int(input("Enter a non-negative integer: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# function calling
print("Factorial number", number, factorial(number))


# Write a Python function to find the maximum of three numbers.

def maxnum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# function calling
num1 = 10
num2 = 25
num3 = 15
maximum = maxnum(num1, num2, num3)
print(f"Maximum no ={maximum}")

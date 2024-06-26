#Definitions for the Basic Arithmetic Operations program.
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

#Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


#Operational methods
add_result = addition(num1, num2)
sub_result = subtraction(num1, num2)
mul_result = multiplication(num1, num2)
div_result = division(num1, num2)


#Print the results to the screen
print(f"The result for addition: {num1} + {num2} = {add_result}")
print(f"The result for subtraction: {num1} - {num2} = {sub_result}")
print(f"The result for addition: {num1} + {num2} = {mul_result}")
print(f"The result for subtraction: {num1} / {num2} = {div_result}")

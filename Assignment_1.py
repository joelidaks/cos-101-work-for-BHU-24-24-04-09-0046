print("Welcome to COS_101")
print("Name: Idakwoji Joel")
print("matric num: BHU24/20/09/0046")
# Define functions for each operation
def add(num1, num2):
    result = int(num1 + num2)
    return result


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    if num2 == 0:
        raise ValueError('Cannot divide by 0')
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


def raise_to_power(num1, num2):
    return num1 ** num2


# Options for user to choose the operation
options = """
1. addition
2. subtraction
3. divide
4. multiply
5. raise_to_power
"""
print(options)

# Get user input for operation
action = int(input("What action do you want to perform (1-5): "))  # Convert input to int
num1 = float(input('Input value one: '))
num2 = float(input('Input value two: '))

# Conditions to perform the chosen operation
if action == 1:
    print("Addition active")
    print(add(num1, num2))

elif action == 2:
    print("Subtraction active")
    print(subtract(num1, num2))

elif action == 3:
    print('Divide active')
    try:
        print(divide(num1, num2))
    except ValueError as e:
        print(e)

elif action == 4:
    print('Multiply active')
    print(multiply(num1, num2))

elif action == 5:
    print('Raise to power active')
    print(raise_to_power(num1, num2))

else:
    print("Invalid choice! Please choose a number between 1 and 5.")

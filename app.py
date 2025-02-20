def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def percentage(x, y):
    if y == 0:
        return "Error! Division by zero."
    return (x / y) * 100

def calculator():
    """
    A simple calculator function that allows the user to perform basic arithmetic operations.

    The user can select from the following operations:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Percentage

    The function prompts the user to enter their choice of operation and two numbers, then performs the selected operation and prints the result.

    Functions used:
    - add(num1, num2): Returns the sum of num1 and num2.
    - subtract(num1, num2): Returns the difference between num1 and num2.
    - multiply(num1, num2): Returns the product of num1 and num2.
    - divide(num1, num2): Returns the quotient of num1 divided by num2.
    - percentage(num1, num2): Returns the percentage of num1 with respect to num2.

    If the user enters an invalid choice, the function prints an "Invalid input" message.
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} is {percentage(num1, num2)}% of {num2}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()
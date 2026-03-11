# Functions for operations
def addition(a, b):
    print("Result:", a + b)

def subtraction(a, b):
    print("Result:", a - b)

def multiplication(a, b):
    print("Result:", a * b)

def division(a, b):
    if b != 0:
        print("Result:", a / b)
    else:
        print("Division by zero not allowed")

def modulus(a, b):
    print("Result:", a % b)

# Menu driven program
while True:
    print("\n---- CALC MENU ----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("Exiting...")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        addition(a, b)
    elif choice == 2:
        subtraction(a, b)
    elif choice == 3:
        multiplication(a, b)
    elif choice == 4:
        division(a, b)
    elif choice == 5:
        modulus(a, b)
    else:
        print("Invalid choice")
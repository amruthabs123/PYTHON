# Define a function for addition
def add(x, y):
    return x + y

# Define a function for subtraction
def subtract(x, y):
    return x - y

# Define a function for multiplication
def multiply(x, y):
    return x * y

# Define a function for division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    else:
        return x / y

# Define a function for modulus
def modulus(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    else:
        return x % y

# Define a function for exponentiation
def exponent(x, y):
    return x ** y

# Define a function for floor division
def floor_divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    else:
        return x // y

# Main function
def main():
    print("Mathematical Operators Program")
    print("-------------------------------")

    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Floor Division")
        print("8. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == "2":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == "3":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == "4":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        elif choice == "5":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"{num1} % {num2} = {modulus(num1, num2)}")

        elif choice == "6":
            num1 = float(input("Enter the base number: "))
            num2 = float(input("Enter the exponent: "))
            print(f"{num1} ^ {num2} = {exponent(num1, num2)}")

        elif choice == "7":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"{num1} // {num2} = {floor_divide(num1, num2)}")

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
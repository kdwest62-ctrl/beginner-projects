import math

print("1. Simple\n2. Scientific\n3. Exit")
while True:
    choice = input("Calculator: ")
    if choice == '1':
        try:
            print("Operators: + - * /")
            operator = input("Select operator: ")
            num1 = float(input("Input number: "))
            num2 = float(input("Input number: "))
            if operator ==  "+":
                print(f"{num1 + num2}")
            elif operator == "-":
                print(f"{num1 - num2}")
            elif operator == "*":
                print(f"{num1 * num2}")
            elif operator == "/":
                print(f"{num1 / num2}")
            else:
                print("Please select an available operator")
        except ValueError:
            print("Input a valid number")
        except ZeroDivisionError:
            print("Cannot divide a number by zero")
    elif choice == '2':
        try:
            print("1. Power, 2. Square Root, 3. Cube Root, 4. Factorial")
            operator = input("Select operator: ")
            num = float(input("Input number: "))
            if operator == '1':
                power = float(input("Power: "))
                print(num ** power)
            elif operator == '2':
                print(num ** (1 / 2))
            elif operator == '3':
                print(num ** (1 / 3))
            elif operator == '4':
                print(math.factorial(num))
            else:
                print("Invalid operator")
        except ValueError:
            print("Input a valid number")
    elif choice == '3':
        print("Program closed")
        break
    else:
        print("Invalid choice")

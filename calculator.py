print("1. Simple\n2. Scientific\n3. Exit")

while True:
    choice = input("Calculator: ")
    if choice == '1':
        try:
            num1 = float(input("Input number: "))
            num2 = float(input("Input number: "))
            print("Operators: + - * /")
            operator = input("Select operator: ")
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
        print("1. Power, 2. Square Root, 3. Cube Root")
        operator = input("Select operator: ")
        if operator == '1':
            num = float(input("Input number: "))
            power = float(input("Power: "))
            print(num ** power)
        elif operator == '2':
            num = float(input("Input number: "))
            print(num ** (1 / 2))
        elif operator == '3':
            num = float(input("Input number: "))
            print(num ** (1 / 3))
        else:
            print("Invalid operator")
    elif choice == '3':
        print("Program closed")
        break
    else:
        print("Please enter a valid choice")

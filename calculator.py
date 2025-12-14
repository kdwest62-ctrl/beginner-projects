num1 = float(input("Input number: "))
num2 = float(input("Input number: "))
print("Available operators: + - * /")
operator = input("Select operator: ")
if operator ==  "+":
    print(f"Result: {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1 * num2}")
elif operator == "/":
    print(f"Result: {num1 / num2}")
else:
    print("Please select an available operator")

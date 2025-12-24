amount = int(input("Enter amount: "))
print("Currencies: php, usd, euro")
source = input("Source currency: ")
if source == 'php':
    target = input("Target currency: ")
    if target == 'usd':
        result = amount * 0.017
        print(f"{amount} Php is equals to {result} USD")
    elif target == 'euro':
        result = amount * 0.015
        print(f"{amount} Php is equals to {result} Euro")
    else:
        print("Invalid target currency")
elif source == 'usd':
    target = input("Target currency: ")
    if target == 'php':
        result = amount * 58.69
        print(f"{amount} USD is equals to {result} Php")
    elif target == 'euro':
        result = amount * 0.85
        print(f"{amount} USD is equals to {result} Euro")
    else:
        print("Invalid target currency")
elif source == 'euro':
    target = input("Target currency: ")
    if target == 'php':
        result = amount * 68.78
        print(f"{amount} Euro is equals to {result} Php")
    elif target == 'usd':
        result = amount * 1.17
        print(f"{amount} Euro is equals to {result} USD")
    else:
        print("Invalid target currency")
else:
    print("Invalid source currency")

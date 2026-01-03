def currency_converter(amt, src, tgt):
    result = src[tgt] * amt
    return result

php = {'USD': 0.017, 'EURO': 0.015}
usd = {'PHP': 58.69, 'EURO': 0.85}
euro = {'PHP': 68.78, 'USD': 1.17}

print("[php, usd, euro]")
source = input("Source currency: ")
amount = int(input("Enter amount: "))
count = input("Number of target currencies (max=2): ")
print("[PHP, USD, EURO]")
if count == '1':
    target = input("Target currency: ")
    if source == 'php':
        print(f"{amount} {source} = {currency_converter(amount, php, target)} {target}")
    elif source == 'usd':
        print(f"{amount} {source} = {currency_converter(amount, usd, target)} {target}")
    elif source == 'euro':
        print(f"{amount} {source} = {currency_converter(amount, euro, target)} {target}")
    else:
        print("Invalid source currency")
elif count == '2':
    target1 = input("Target currency 1: ")
    target2 = input("Target currency 2: ")
    if source == 'php':
        print(f"{amount} {source} = {currency_converter(amount, php, target1)} {target1}")
        print(f"{amount} {source} = {currency_converter(amount, php, target2)} {target2}")
    elif source == 'usd':
        print(f"{amount} {source} = {currency_converter(amount, usd, target1)} {target1}")
        print(f"{amount} {source} = {currency_converter(amount, usd, target2)} {target2}")
    elif source == 'euro':
        print(f"{amount} {source} = {currency_converter(amount, euro, target1)} {target1}")
        print(f"{amount} {source} = {currency_converter(amount, euro, target2)} {target2}")
    else:
        print("Invalid source currency")
else:
    print("Only 2 target currencies are allowed")

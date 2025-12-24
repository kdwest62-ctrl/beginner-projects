fibonacci = [0, 1]
sequence = int(input("Input sequence: "))
if sequence <= 0:
    print("Invalid input")
elif sequence == 1:
    print("[0]")
elif sequence == 2:
    print(fibonacci)
else:
    while len(fibonacci) != sequence:
        num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(num)
    print(fibonacci)

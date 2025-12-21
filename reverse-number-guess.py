import random

num = random.randint(1, 5)
attempt = 1
print("Think of a number from 1 to 5\nLet's see how many attempts I can guess it")
while True:
    print(num)
    choice = input("Higher, lower, or OK? (h/l/ok): ")
    if choice == "ok":
        break
    elif choice == "h":
        num += 1
        attempt += 1
    elif choice == "l":
        num -= 1
        attempt += 1
    else:
        print("Please answer the question correctly")
print(f"I guessed your number in {attempt} attempts")

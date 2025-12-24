import random

min_num = int(input("Input minimum number: "))
max_num = int(input("Input maximum number: "))
num = random.randint(min_num, max_num)
attempt = 1
print(f"Think of a number from {min_num} to {max_num}")
print("Let's see how many attempts I can guess it")
while True:
    print(num)
    choice = input("Higher, lower, or OK? (h/l/ok): ")
    if choice == "ok":
        break
    elif choice == "h":
        increment = random.randint(1, 2)
        num += increment
        attempt += 1
    elif choice == "l":
        increment = random.randint(1, 2)
        num -= increment
        attempt += 1
    else:
        print("Please answer correctly")
print(f"I guessed your number in {attempt} attempts")

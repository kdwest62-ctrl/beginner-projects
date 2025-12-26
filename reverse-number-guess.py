import random

min_num = int(input("Input minimum number: "))
max_num = int(input("Input maximum number: "))
num = random.randint(min_num, max_num)

limit = int(input("Input limit (attempts): "))
attempt = 1
print(f"Think of a number from {min_num} to {max_num}")
print(f"Let's see I can guess it in {limit} attempts")
while attempt != limit:
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
if attempt == limit:
    print("Human wins")
else:
    print("CPU wins")

import random

def random_num(start, stop, avoid):
    num_list = []
    for element in range(start, stop + 1):
        num_list.append(element)
    for item in num_list:
        if item in avoid:
            num_list.remove(item)
    num = random.choice(num_list)
    return num

cpu_nums = []
avoid_nums = []
min_num = int(input("Minimum number: "))
max_num = int(input("Maximum number: "))
print(f"Think of a number from {min_num} to {max_num}")
player_num = random.randint(min_num, max_num)
cpu_nums.append(player_num)

limit = int(input("Limit (attempts): "))
attempt = 0
while attempt != limit:
    cpu_guess = cpu_nums[-1]
    print(cpu_guess)
    choice = input("Is this your number? (y/n): ")
    if choice == "y":
        attempt += 1
        break
    elif choice == "n":
        attempt += 1
        avoid_nums.append(cpu_guess)
        cpu_nums.append(random_num(min_num, max_num, avoid_nums))
    else:
        attempt += 1
        print("Invalid answer")

if attempt == limit:
    print("You win")
else:
    print("CPU wins")

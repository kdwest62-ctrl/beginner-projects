import random

min_num = int(input("Input minimum number: "))
max_num = int(input("Input maximum number: "))
num = random.randint(min_num, max_num)
attempt = 0

limit = int(input("Set the limit (attempts): "))
while attempt != limit:
    try:
        guess = int(input(f"Guess the number (between {min_num} and {max_num}): "))
        if guess < num:
            print("Too low!")
            attempt += 1
        elif guess > num:
            print("Too high!")
            attempt += 1
        else:
            print("Congratulations! You guessed the number")
            exit()
    except ValueError:
        print("Please enter a valid number")
        attempt += 1
if attempt == limit:
    print(f"You lost. The correct number is {num}")

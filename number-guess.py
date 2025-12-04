import random

num = random.randint(1, 10)
attempt = 0

while True:
    try:
        guess = int(input(f"Guess the number (1-10): "))
        if guess < num:
            print("Too low!")
            attempt += 1
        elif guess > num:
            print("Too high!")
            attempt += 1
        else:
            attempt += 1
            break
    except ValueError:
        print("Please enter a valid number")
        attempt += 1
print(f"Congratulations! You guessed the number in {attempt} attempts")

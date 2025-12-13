import random

rand_num = str(random.randint(1000, 9999))

while True:
    bulls = 0
    cows = 0
    guess_num = input("Guess the number: ")
    if guess_num == rand_num:
        print("Congratulations! You have guessed the number")
        break
    else:
        for item in guess_num:
            if item in rand_num:
                if rand_num.index(item) == guess_num.index(item):
                    bulls += 1
                else:
                    cows += 1
            else:
                continue
        print(f"Cows: {cows}, Bulls: {bulls}")

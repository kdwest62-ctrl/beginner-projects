import random

rand_num = str(random.randint(1000, 9999))
attempt = 0

while True:
    bulls = 0
    cows = 0
    guess_num = input("Guess the number: ")
    if guess_num == rand_num:
        attempt += 1
        print(f"Well done! You have guessed the number. You did it in {attempt} attempts")
        break
    else:
        for item in guess_num:
            if item in rand_num:
                if guess_num.index(item) == rand_num.index(item):
                    bulls += 1
                else:
                    cows += 1
            else:
                continue
        attempt += 1
        print(f"Cows: {cows}, Bulls: {bulls}")

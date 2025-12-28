import random

rand_list = []
length = int(input("Length of random number: "))
count = 0
while length != count:
    num = random.randint(0, 9)
    rand_list.append(str(num))
    count += 1
rand_num = "".join(rand_list)
rand_dict = dict(enumerate(rand_num))

attempt = 0
while True:
    bulls = 0
    cows = 0
    guess_num = input(f"Guess the {length}-digit number: ")
    guess_dict = dict(enumerate(guess_num))
    if guess_dict == rand_dict:
        attempt += 1
        print(f"Well done! You have guessed the number. You did it in {attempt} attempts")
        break
    else:
        attempt += 1
        for key in guess_dict:
            if guess_dict[key] in rand_dict.values():
                if guess_dict[key] == rand_dict[key]:
                    bulls += 1
                else:
                    cows += 1
            else:
                continue
        print(f"Cows: {cows}, Bulls: {bulls}")

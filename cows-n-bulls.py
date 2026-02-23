import random

try:
    length = int(input("Length of random number: "))
    if length != 0:
        digits = []
        count = 0
        while count != length:
            num = random.randint(0, 9)
            digits.append(str(num))
            count += 1
        rand_num = "".join(digits)
        rand_num_with_index = dict(enumerate(rand_num))

        attempt = 0
        wrong_guess = 0
        while True:
            bulls = 0
            cows = 0
            guess_num = input(f"Guess the {length}-digit number: ")
            if len(guess_num) > length:
                print("Invalid length")
                attempt += 1
            else:
                guess_with_index = dict(enumerate(guess_num))
                if guess_num == rand_num:
                    attempt += 1
                    print(f"Well done! You have guessed the number\nIt took {attempt} attempts")
                    break
                else:
                    attempt += 1
                    wrong_guess += 1
                    for digit in guess_with_index:
                        if guess_with_index[digit] in rand_num_with_index.values():
                            if guess_with_index[digit] == rand_num_with_index[digit]:
                                bulls += 1
                            else:
                                cows += 1
                    print(f"Cows: {cows}, Bulls: {bulls}")
                if wrong_guess == 5:
                    print(f"Hint: first digit = {rand_num_with_index[0]}")
except ValueError:
    print("Please input a number")

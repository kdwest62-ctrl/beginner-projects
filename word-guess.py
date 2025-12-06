word = "python"

print("_ _ _ _ _ _")

while True:
    letter = input("Enter a letter: ")
    if letter == "p":
        print("Good guess")
        print("p _ _ _ _ _")
        decision = input("Guess the word (y/n): ")
        if decision == "y":
            guess_word = input("Word: ")
            if guess_word == word:
                break
            else:
                print("Wrong word")
        elif decision == "n":
            continue
        else:
            print("Please input a valid answer")

    elif letter == "y":
        print("Good guess")
        print("_ y _ _ _ _")
        decision = input("Guess the word (y/n): ")
        if decision == "y":
            guess_word = input("Word: ")
            if guess_word == word:
                break
            else:
                print("Wrong word")
        elif decision == "n":
            continue
        else:
            print("Please input a valid answer")

    elif letter == "t":
        print("Good guess")
        print("_ _ t _ _ _")
        decision = input("Guess the word (y/n): ")
        if decision == "y":
            guess_word = input("Word: ")
            if guess_word == word:
                break
            else:
                print("Wrong word")
        elif decision == "n":
            continue
        else:
            print("Please input a valid answer")

    elif letter == "h":
        print("Good guess")
        print("_ _ _ _h _ _")
        decision = input("Guess the word (y/n): ")
        if decision == "y":
            guess_word = input("Word: ")
            if guess_word == word:
                break
            else:
                print("Wrong word")
        elif decision == "n":
            continue
        else:
            print("Please input a valid answer")

    elif letter == "o":
        print("Good guess")
        print("_ _ _ _ o _")
        decision = input("Guess the word (y/n): ")
        if decision == "y":
            guess_word = input("Word: ")
            if guess_word == word:
                break
            else:
                print("Wrong word")
        elif decision == "n":
            continue
        else:
            print("Please input a valid answer")

    elif letter == "n":
        print("Good guess")
        print("_ _ _ _ _ n")
        decision = input("Guess the word (y/n): ")
        if decision == "y":
            guess_word = input("Word: ")
            if guess_word == word:
                break
            else:
                print("Wrong word")
        elif decision == "n":
            continue
        else:
            print("Please input a valid answer")

    else:
        print("Wrong guess")

print("Congratulations! You have guessed the word")

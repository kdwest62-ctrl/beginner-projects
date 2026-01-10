keys = []
words = {'Easy': 'set', 'Medium': 'tuple', 'Hard': 'module'}
print("1. Easy, 2. Medium, 3. Hard")
choice = input("Select difficulty: ")
if choice == '1':
    word = words['Easy']
    for letter in word:
        keys.append(letter)
elif choice == '2':
    word = words['Medium']
    for letter in word:
        keys.append(letter)
elif choice =='3':
    word = words['Hard']
    for letter in word:
        keys.append(letter)
else:
    print("Invalid input")

if len(keys) != 0:
    values = []
    count = 0
    while count != len(keys):
        values.append('_')
        count += 1
    word_to_guess = dict(zip(keys, values))

    score = 0
    while score != len(word_to_guess):
        print(list(word_to_guess.values()))
        guess = input("Guess a letter: ")
        if guess in word_to_guess.keys():
            print("Correct guess")
            score += 1
            update = {guess: guess}
            word_to_guess.update(update)
        else:
            print("Wrong guess")
    print(list(word_to_guess.values()))
    print("Well done! You have guessed the word")

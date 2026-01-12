keys = []
words = ['list', 'tuple', 'module']
print("1. Easy, 2. Medium, 3. Hard")
difficulty = input("Select difficulty: ")
if difficulty == '1':
    for letter in words[0]:
        keys.append(letter)
elif difficulty == '2':
    for letter in words[1]:
        keys.append(letter)
elif difficulty == '3':
    for letter in words[2]:
        keys.append(letter)
else:
    print("Invalid input")

if len(keys) != 0:
    values = []
    count = 0
    while count != len(keys):
       values.append('-')
       count += 1
    word_to_guess = dict(zip(keys, values))

    attempt = 0
    score = 0
    while score != len(word_to_guess):
       print("".join(word_to_guess.values()))
       guess = input("Guess a letter: ")
       if guess in word_to_guess.keys():
           print("Correct guess")
           attempt += 1
           score += 1
           update = {guess: guess}
           word_to_guess.update(update)
       else:
           print("Wrong guess")
           attempt += 1
    print("".join(word_to_guess.values()))
    print(f"Well done! You have guessed the word\nYou did it in {attempt} attempts")

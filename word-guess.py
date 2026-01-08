keys = []
words = ['list', 'tuple', 'string']
choice = input("Select word (1/2/3): ")
if choice == '1':
    word = words[0]
    for letter in word:
        keys.append(letter)
elif choice == '2':
    word = words[1]
    for letter in word:
        keys.append(letter)
elif choice =='3':
    word = words[2]
    for letter in word:
        keys.append(letter)
else:
    print("Wrong choice")

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

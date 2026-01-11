import random

keys = []
words = ['string', 'tuples', 'module', 'random']
word = random.choice(words)
for letter in word:
    keys.append(letter)

values = []
count = 0
while count != len(keys):
    values.append('_')
    count += 1
word_to_guess = dict(zip(keys, values))

attempt = 0
score = 0
while score != len(word_to_guess):
    print(list(word_to_guess.values()))
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
print(list(word_to_guess.values()))
print(f"Well done! You have guessed the word\nYou did it in {attempt} attempts")

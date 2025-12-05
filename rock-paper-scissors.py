import random

cpu_score = 0
player_score = 0

while player_score != 5 and cpu_score != 5:
    player = input("Rock, paper, or scissors? (r/p/s): ")
    cpu = random.choice(['r', 'p', 's'])
    if player == 'r' and cpu == 's':
        print(f"You: {player} | CPU: {cpu}")
        print("You win")
        player_score += 1
        print(f"Scores: Player = {player_score}, CPU = {cpu_score}")
    elif player == 'p' and cpu == 'r':
        print(f"You: {player} | CPU: {cpu}")
        print("You win")
        player_score += 1
        print(f"Scores: Player = {player_score}, CPU = {cpu_score}")
    elif player == 's' and cpu == 'p':
        print(f"You: {player} | CPU: {cpu}")
        print("You win")
        player_score += 1
        print(f"Scores: Player = {player_score}, CPU = {cpu_score}")
    elif player == 'r' and cpu == 'p':
        print(f"You: {player} | CPU: {cpu}")
        print("You lose")
        cpu_score += 1
        print(f"Scores: Player = {player_score}, CPU = {cpu_score}")
    elif player == 'p' and cpu == 's':
        print(f"You: {player} | CPU: {cpu}")
        print("You lose")
        cpu_score += 1
        print(f"Scores: Player = {player_score}, CPU = {cpu_score}")
    elif player == 's' and cpu == 'r':
        print(f"You: {player} | CPU: {cpu}")
        print("You lose")
        cpu_score += 1
        print(f"Scores: Player = {player_score}, CPU = {cpu_score}")
    elif player == 'r' and cpu == 'r':
        print(f"You: {player} | CPU: {cpu}")
        print("Tie")
        print(f"Scores: Player = {player_score}, CPU = {cpu_score}")
    elif player == 'p' and cpu == 'p':
        print(f"You: {player} | CPU: {cpu}")
        print("Tie")
        print(f"Scores: Player = {player_score}, CPU = {cpu_score}")
    elif player == 's' and cpu == 's':
        print(f"You: {player} | CPU: {cpu}")
        print("Tie")
        print(f"Scores: Player = {player_score}, CPU = {cpu_score}")
    else:
        print("Invalid input")
        print(f"Scores: Player = {player_score}, CPU = {cpu_score}")

print("Game over!")
if player_score == 5:
    print(f"Player wins")
else:
    print(f"CPU wins")

import random

cpu_score = 0
player_score = 0
max_point = int(input("Enter max points to win: "))

while player_score != max_point and cpu_score != max_point:
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
        print("CPU wins")
        cpu_score += 1
        print(f"Scores: Player = {player_score}, CPU = {cpu_score}")
    elif player == 'p' and cpu == 's':
        print(f"You: {player} | CPU: {cpu}")
        print("CPU wins")
        cpu_score += 1
        print(f"Scores: Player = {player_score}, CPU = {cpu_score}")
    elif player == 's' and cpu == 'r':
        print(f"You: {player} | CPU: {cpu}")
        print("CPU wins")
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
if player_score == max_point:
    print("Player wins")
else:
    print("CPU wins")

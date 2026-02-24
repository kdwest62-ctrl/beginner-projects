import random

try:
    def score(human, robot):
        if human == 'r' and robot == 's':
            return "Player"
        elif human == 'p' and robot == 'r':
            return "Player"
        elif human == 's' and robot == 'p':
            return "Player"
        elif human == 'r' and robot == 'p':
            return "CPU"
        elif human == 'p' and robot == 's':
            return "CPU"
        elif human == 's' and robot == 'r':
            return "CPU"
        elif human == 'r' and robot == 'r':
            return "Tie"
        elif human == 'p' and robot == 'p':
            return "Tie"
        elif human == 's' and robot== 's':
            return "Tie"
        else:
            return "Invalid input"

    cpu_score = 0
    player_score = 0
    max_score = int(input("Enter max score to win: "))
    if max_score != 0:
        while player_score != max_score and cpu_score != max_score:
            player = input("Rock, paper, or scissors? (r/p/s): ")
            cpu = random.choice(['r', 'p', 's'])
            print(f"Player: {player} | CPU: {cpu}")
            print(score(player, cpu))
            if score(player, cpu) == "Player":
                player_score += 1
            elif score(player, cpu) == "CPU":
                cpu_score += 1
            print(f"Scores: Player = {player_score}, CPU = {cpu_score}")
        print("Game over!")
        if player_score == max_score:
            print("Player wins")
        elif cpu_score == max_score:
            print("CPU wins")
except ValueError:
    print("Please input a number")

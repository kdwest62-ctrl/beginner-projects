import random

max_points = int(input("Input maximum points to win: "))

player1 = 0
player2 = 0

while True:
    turn1 = []
    while True:
        print("Player 1")
        roll = input("Roll? (y/n): ")
        if roll == 'y' or roll == 'Y':
            num = random.randint(1, 6)
            if num == 1:
                print(f"You rolled a {num}")
                print("Score: 0")
                turn1.clear()
                player1 += sum(turn1)
                break
            elif num == 6:
                if len(turn1) != 0:
                    if turn1[-1] == 6:
                        print(f"You rolled a {num}")
                        print("You rolled two 6's in a row")
                        print("Score: 0")
                        turn1.clear()
                        player1 += sum(turn1)
                        break
                    else:
                        print(f"You rolled a {num}")
                        turn1.append(num)
                else:
                    print(f"You rolled a {num}")
                    turn1.append(num)
            else:
                print(f"You rolled a {num}")
                turn1.append(num)
        elif roll == 'n' or roll == 'N':
            player1 += sum(turn1)
            break
        else:
            print("Please input a valid answer")

    if player1 >= max_points:
        print(f"Current scores: Player 1 = {player1}, Player 2 = {player2}")
        print("Player 1 wins")
        break
    elif player2 >= max_points:
        print(f"Current scores: Player 1 = {player1}, Player 2 = {player2}")
        print("Player 2 wins")
        break
    else:
        print(f"Current scores: Player 1 = {player1}, Player 2 = {player2}")

    turn2 = []
    while True:
        print("Player 2")
        roll = input("Roll? (y/n): ")
        if roll == 'y' or roll == 'Y':
            num = random.randint(1, 6)
            if num == 1:
                print(f"You rolled a {num}")
                print("Score: 0")
                turn2.clear()
                player2 += sum(turn2)
                break
            elif num == 6:
                if len(turn2) != 0:
                    if turn2[-1] == 6:
                        print(f"You rolled a {num}")
                        print("You rolled two 6's in a row")
                        print("Score: 0")
                        turn2.clear()
                        player2 += sum(turn2)
                        break
                    else:
                        print(f"You rolled a {num}")
                        turn2.append(num)
                else:
                    print(f"You rolled a {num}")
                    turn2.append(num)
            else:
                print(f"You rolled a {num}")
                turn2.append(num)
        elif roll == 'n' or roll == 'N':
            player2 += sum(turn2)
            break
        else:
            print("Please input a valid answer")

    if player1 >= max_points:
        print(f"Current scores: Player 1 = {player1}, Player 2 = {player2}")
        print("Player 1 wins")
        break
    elif player2 >= max_points:
        print(f"Current scores: Player 1 = {player1}, Player 2 = {player2}")
        print("Player 2 wins")
        break
    else:
        print(f"Current scores: Player 1 = {player1}, Player 2 = {player2}")

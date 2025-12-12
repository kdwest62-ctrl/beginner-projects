import random

def bet_multiply(n1, n2, n3, b):
    if n1 == n2 == n3:
        return b * 10
    elif n1 == n2 or n2 == n3 or n3 == n1:
        return b * 2
    elif n1 != n2 != n3:
        return 0
    else:
        return b

current_bal = 0
starting_bal = int(input("Enter your starting balance: $"))
current_bal += starting_bal
print("Welcome to the Slot Machine Game")
print(f"You start with a balance of ${starting_bal}")

while True:
    print(f"Current balance: ${current_bal}")
    if current_bal == 0:
        print(f"You currently have ${current_bal} balance")
        print("Game over")
        break
    bet = int(input("Enter your bet amount: $"))
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)
    print(f"{num1} | {num2} | {num3}")
    winnings = bet_multiply(num1, num2, num3, bet)
    print(f"You won ${winnings}")
    if winnings == 0:
        current_bal -= bet
    else:
        current_bal += (bet_multiply(num1, num2, num3, bet))
    if current_bal == 0:
        print(f"You currently have ${current_bal} balance")
        print("Game over")
        break
    else:
        user_decide = input("Do you want to play again? (y/n): ")
        if user_decide == "n":
            break

print("Thank you for playing")

import random

while True:
    roll_dice = input("Roll the dice? (y/n): ")
    if roll_dice == "y" or roll_dice == "Y":
        num1 = random.randint(1, 7)
        num2 = random.randint(1, 7)
        print(f"({num1}, {num2})")
    elif roll_dice == "n" or roll_dice == "N":
        break
    else:
        print("Invalid choice!")
print("Thanks for playing!")

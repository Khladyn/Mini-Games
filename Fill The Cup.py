import random

# The goal of this game is to beat the computer into reaching a secret sum.
# The player and the computer will enter a random number which will be added to their cups,
# whoever reaches the brim first, wins. Whoever exceeds the brim, loses.

print("Fill the cup before the computer does!")

brim = random.randint(10, 20)

# for drop in range(brim):
#     print(drop)

players_cup = 0
computers_cup = 0

while computers_cup < brim:
    drop = int(input("How many drops? "))
    players_cup += drop
    computers_cup += random.randint(1, 10)

    if players_cup > brim:
        print("Nooo! The cup overflowed!")
        print(f"Brim: {brim}")
        break

    elif players_cup == brim:
        print("Congratulations! You filled the cup!")
        print(f"Brim: {brim}")
        break

    elif brim - computers_cup < 5:
        computers_cup += brim - computers_cup
        print("Sad... the computer beat you to it.")

    elif brim - players_cup < 5:
        print("Almost there...")

    else:
        print("Keep going...")

    print(f"P: {players_cup}")
    print(f"C: {computers_cup}")
import random

"""
The goal of this game is to eliminate all non-zero digits by adding or
removing an element from the list. The rule is, a digit can be removed from
the list if it exists as many times as itself. Example: 3 can be removed from
the list if it appears 3 times. So the player has to add or delete a number
from 0-5 to satisfy this condition, and eventually arrive at an all-zero list.
"""

line = []

for n in range(20):
    n = random.randint(0, 5)
    line.append(n)

print(line)

while any(line):

    operation = input("\nAdd (A) or Delete (D) ? ")
    number = int(input("Enter a number (0-5): "))

    if operation.upper() == "A":
        line.append(number)

    elif operation.upper() == "D":
        line.remove(number)

    else:
        print("Invalid input.")
        continue

    for r in range(1, 6):
        if line.count(r) == r:
            line = [l for l in line if l != r]

    if len(line) > 5 and len(line) % 2 == 0:
        line.append(random.randint(1, 5))

    print(f"\n{line}")

else:
    print("\nYay! We're having ice cream today!")
import random
"""
The city is being terrorized by a mafia of 14 members in 7 various ranks. The highest ranking member
can inflict damage costing 10 million pesos while the second in command, a million less and so on.
Only the lowest ranking member called the "Associate" can vary between 1-4 million pesos worth of damage.

This family only commit crimes in groups of 3-5, and the goal of this game is to identify which ones
are involved in a crime. Clues will be given throughout the game. The game begins with a chart of the mafia
hierarchy and the amount of damage they can inflict. The total damage is the sum of each criminal's participation.

First, the player is given the chance to guess the mastermind. If they get it right, then the game is won.
If not, then the player will proceed to guess all the names of those involved. Take note that for each turn,
the player must enter all names of the suspects in one line separated by spaces, and not one at a time.

There is a counter for correct guesses, but only a clue will appear for how many names are guessed
incorrectly by the player. Each criminal gets closer to the city border with each turn, and the player
must catch all criminals before they escape. Any criminal who manages to escape will be revealed
to the player, serving as a clue as to how much the total damage can be subtracted by.

If all criminals have escaped before the player has identified them, then the game is lost.
If the player manages to get some or all of them correctly before they escape, then the player wins the game.
"""

the_mafia = {
    "Godfather": 10,
    "Boss": 9,
    "Underboss": 8,
    "Consigliere": 7,
    "Caporegime_1": 6,
    "Caporegime_2": 6,
    "Caporegime_3": 6,
    "Soldier_1": 5,
    "Soldier_2": 5,
    "Soldier_3": 5,
    "Soldier_4": 5,
    "Soldier_5": 5,
    "Soldier_6": 5,
    "Associate": 0
}

the_mafia["Associate"] = random.randint(1, 4)

total_damage = 0
crime_area = 11

group_limit = 5
crime_group = {}

print("\nAbout The Mafia:")
for m in the_mafia:
    if m == "Associate":
        print(f"Associate varies between 1-4 million peso/s.")
        continue
    print(f"{m} can inflict {the_mafia[m]} million worth of damages.")

for x in range(group_limit):
    criminal = random.choice(list(the_mafia.keys()))
    if criminal not in crime_group:
        crime_group[criminal] = the_mafia[criminal]
        total_damage += crime_group[criminal]

group_ranked = dict(sorted(crime_group.items(), key=lambda x:x[1]))
print("\nThe mafia has attacked again! The city needs your help.")

mastermind = list(group_ranked.keys())[-1]
print(f"\nThere were {len(group_ranked)} people involved in the crime.")
print(f"The total damage is worth {total_damage} million pesos.")

user_mastermind = input("\nWho's the mastermind? ")

if user_mastermind.lower() == mastermind.lower():
    print("\nExcellent work! You've caught the mastermind. Now the rest will come save him.")

else:
    print(f"\nIncorrect. {user_mastermind} is not the mastermind.")

    user_group = []
    group_innocent = set()
    missing_criminals = 0

    while sorted(user_group) != sorted(list(crime_group.keys())):

        user_group = (input("\nWho are involved? ").split())
        
        for u in user_group:
            if u not in list(crime_group.keys()):
                group_innocent.add(u)

        if len(group_innocent) > 0:
            print("\n{} is/are not involved in the crime.".format(", ".join([f"and {i}"
                if len(group_innocent) > 1 and list(group_innocent).index(i) == len(group_innocent)-1
                else i for i in group_innocent])))
        
            group_innocent.clear()

        for c in list(crime_group.keys()):
            if c not in user_group:
                missing_criminals += 1

        if missing_criminals > 0:
            print(f"\nYou are missing {missing_criminals} more criminal/s.")

        missing_criminals = 0
        
        for r in group_ranked.copy():
            group_ranked[r] += 1
            if group_ranked[r] >= crime_area:
                print(f"\n{r} has run away!")
                group_ranked.pop(r)

        if len(group_ranked) < 1:
            print(f"\nGame over. The criminals have all escaped. The mastermind is {mastermind}.")
            break

    else:
        if sorted(user_group) == sorted(list(group_ranked.keys())):
            print("\nGreat job! You've identified the criminals.")
        else:
            print("\nYou've identified the remaining criminals, but do better next time.")
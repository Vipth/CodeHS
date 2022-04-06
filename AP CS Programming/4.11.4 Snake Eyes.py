import random

# Variables
rolls = 0

while True:
    rolls += 1
    diceOne = random.randint(1, 6)
    diceTwo = random.randint(1, 6)
    print(f"Rolled: {diceOne} {diceTwo}")
    if diceOne == 1 and diceTwo == 1:
        break
print(f"It took you {rolls} rolls to get snake eyes.")

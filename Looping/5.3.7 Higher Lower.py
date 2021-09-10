"""
This program makes the user guess a number between 1 and 100.
"""

magic_number = 3
# Has the user guess numbers until they get it correct. They will get a hint if 
# they are wrong
while True:
    guess = int(input("Enter a guess: "))
    if guess == magic_number:
        print("Correct!")
        break
    elif guess > magic_number:
        print("Too high!")
    elif guess < magic_number:
        print("Too low!")

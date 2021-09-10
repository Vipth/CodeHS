"""
This program makes the user guess a float between 1 and 100.
"""

my_float = 3.3312
# Has the user guess numbers until they get it correct. They will get a hint if 
# they are wrong
while True:
    guess = float(input("Enter a guess: "))
    if guess == round(my_float, 2):
        print("Correct!")
        break
    elif guess > round(my_float, 2):
        print("Too high!")
    elif guess < round(my_float, 2):
        print("Too low!")

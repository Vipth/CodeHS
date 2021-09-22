secret_word = "Python"
guesses = 10

def get_guess():
    while True:
        guess = input("Guess: ")
        if len(guess) == 1 and type(guess) == str and guess.islower() == True:
            return guess
        else:
            print("Must be a single lowercase letter!")
            
while True:
    if get_guess() not in secret_word.lower():
        guesses -= 1
        if guesses == 0:
            print("Game Over! Out of guesses.")
            break
        print(f"Incorrect! You now have {guesses} guesses left!")

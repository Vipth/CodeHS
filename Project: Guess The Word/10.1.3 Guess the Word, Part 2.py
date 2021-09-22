secret_word = "Python"
dashes = '-' * len(secret_word)
guesses = 10

def get_guess():
    while True:
        guess = input("Guess: ")
        if len(guess) == 1 and type(guess) == str and guess.islower() == True:
            return guess
        else:
            print("Must be a single lowercase letter!")
            
def update_dashes(secret_word, dashes, guess):
    for i in range(len(secret_word)):
        dashes = list(dashes)
        if guess == secret_word[i]:
            if i == 0:
                dashes[i] = guess.upper()
            else:
                dashes[i] = guess
    dashes = ''.join(dashes)
    return dashes
            
while True:
    print(dashes)
    guess = get_guess()
    if guess not in secret_word.lower():
        guesses -= 1
        if guesses == 0:
            print("Game Over! Out of guesses.")
            break
        print(f"That letter is not in the word!")
    else:
        print("That letter is in the word.")
        dashes = update_dashes(secret_word.lower(), dashes, guess)

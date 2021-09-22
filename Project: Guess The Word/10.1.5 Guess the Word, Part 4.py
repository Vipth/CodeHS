import random

secret_words = ["Python", "JavaScript", "Java", "C", "Html", "CSS", "Ruby"]
guesses_left = 10
win = None
def choice():
    secret_word = random.choice(secret_words)
    return secret_word
    
secret_word = choice()
dashes = '-' * len(secret_word)

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
    
    if dashes.lower() == secret_word.lower():
        win = True
    if guesses_left == 0:
        win = False
    if win == True:
        print("Congratulations! You Win.")
        break
    elif win == False:
        print(f"You lose. The word was: {secret_word}.")
        break
    
    print(f"{guesses_left} guesses left.")
    guess = get_guess()
    
    if guess not in secret_word.lower():
        guesses_left -= 1
        print(f"That letter is not in the word!")
    else:
        print("That letter is in the word.")
        dashes = update_dashes(secret_word.lower(), dashes, guess)

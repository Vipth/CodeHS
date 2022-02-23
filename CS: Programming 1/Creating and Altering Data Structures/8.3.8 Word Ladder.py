"""
This program asks the user for an initial word, then repeatedly asks them for an index and letter, and replaces the letter at `index` for `letter`.
"""

def word_latter():
    word = input("Enter a word: ")
    while True:
        index = int(input("Enter an index (-1 to quit): "))
        if index == -1:
            return
        elif index > len(word) or index < -1:
            print("Invalid index")
        else:
            x = False
            while x == False:
                letter = input("Enter a letter: ")
                if letter == letter.upper():
                    print("Character must be a lowercase letter!")
                elif len(letter) > 1:
                    print("Must be exactly one character!")
                else:
                    x = True
            word = list(word)
            word[index] = letter
            word = ''.join(word)
            print(word)
word_latter()

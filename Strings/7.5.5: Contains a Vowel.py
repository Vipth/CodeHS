# Checks to see if an input word contains any vowels.
vowels = ('a','e','i','o','u')

def contains_vowel(word):
    for i in vowels:
        for j in word:
            if i == j:
                return True
    return False

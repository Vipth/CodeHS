# This function returns `word` with all instances of `letter` removed!
def remove_all_from_string(word, letter):
    while letter in word:
        x = word.find(letter)
        letters = list(word)
        letters.remove(letters[x])
        word = ''.join(letters)
    return word

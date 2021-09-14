# update this function to return the number of times `second` appears in `first`!
def count_occurrences(word, character):
    count = 0
    for i in word:
        if i.lower() == character.lower():
            count += 1
    return count

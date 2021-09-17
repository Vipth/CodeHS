# Returns string with the letter at the index, replaced with the letter
# taken as an argument.
def replace_at_index(string, index, letter):
    string = list(string)
    string[index] = letter
    ''.join(string)
    return string

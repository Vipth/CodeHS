"""
This program removes all instances of `phrase` from `string`.
"""

def remove_all_from_string(string, phrase):
    if len(phrase) == 0:
        return string
    while phrase in string:
        phrase_start = string.find(phrase)
        phrase_len = len(phrase)
        string = string[:phrase_start] + string[phrase_start + phrase_len:]
    return string
    
print(remove_all_from_string("bananas", "na"))

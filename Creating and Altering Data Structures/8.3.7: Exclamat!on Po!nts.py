# update this function so it replaces all lowercase 'i's in `text` with '!'
def exclamation(text):
    text = list(text)
    for i, v in enumerate(text):
        if v == 'i':
            text[i] = "!"
    text = ''.join(text)
    return text

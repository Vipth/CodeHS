# this function should return the number of words that contain "owl"!
def owl_count(text):
    owls = 0
    text = text.split()
    for word in text:
        if "owl" in word.lower():
            owls += 1
    return owls

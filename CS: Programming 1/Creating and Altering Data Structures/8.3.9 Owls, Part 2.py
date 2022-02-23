# this function should return the number of words that contain "owl" and the indices that they are at.
def owl_count():
    text = input("Enter some text: ")
    indices = []
    owls = 0
    text = text.split()
    for i, v in enumerate(text):
        if "owl" in v.lower():
            owls += 1
            indices.append(i)
    print(f"There were {owls} words that contained 'owl'.")
    print(f"they occurred at indices: {indices}")
    
owl_count()

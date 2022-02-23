"""
This program asks for text from a user and returns the amount of times any word appears in the text.
"""
text = input("Enter some text: ")
text = text.split()
words = {}
print(text)

for word in text:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
        
print(words)

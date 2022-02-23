"""
This program asks for text from a user and returns the amount of 
times any word appears in the text.
"""
text = input("Enter some text: ")
text = text.split()
words = {}
print(text)

def update_counts(count_dictionary, word):
    if word in count_dictionary:
        count_dictionary[word] += 1
    else:
        count_dictionary[word] = 1

for word in text:
    update_counts(words, word)
        
print(words)

phonebook = {}

while True:
    name = input("Enter a Name: ")
    if name == "":
        break
    
    if name in phonebook:
        print(phonebook[name])
    else:
        number = input("Please enter a phone number: ")
        phonebook[name] = number
print(phonebook)

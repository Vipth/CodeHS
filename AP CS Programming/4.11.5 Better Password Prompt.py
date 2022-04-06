SECRET = "abc123"
# Enter your code here

while True:
    userInput = input("Enter password: ")
    if userInput != SECRET:
        print("Sorry, that did not match. Please try again.")
    else:
        print("You got it!")
        break

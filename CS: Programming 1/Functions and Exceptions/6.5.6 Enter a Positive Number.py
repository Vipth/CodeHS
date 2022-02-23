"""
This program prompts the user to enter a positive number, and throws
an error if their input is not an integer above 0.
"""

def retrieve_positive_number():
    number = None
    while type(number) != int:
        number = input("Please enter a number: ")
        try:
            number = int(number)
            if number < 0:
                print("Please enter a positive number!")
                number = None
            else:
                return number
        except ValueError:
            print("Please enter a positive number!")
            number = None
        
retrieve_positive_number()

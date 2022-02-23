"""
This program tells the user whether the number they choose is positive, zero,
or negative.
"""

# Compares the numbers to see if they're positive, zero, or negative.
number = int(input("Please enter a number: "))
if number >= 1:
    print("That number is positive!")
elif number == 0:
    print("That number is zero!")
else:
    print("That number is negative!")

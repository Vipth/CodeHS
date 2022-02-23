"""
This program calculates the area of a square with a user chosen
side length. If the user inputs an impossible number (0 or lower),
then the default number of 10 is used.
"""

# Calculates the area
def calculate_area(side_length = 10):
    if side_length <= 0:
        side_length = 10
    area = side_length * side_length
    print(f"The area of a square with sides of length {side_length} is {area}.")

# Asks the user for the side length of a square.
side_length = int(input("Enter side length: "))
calculate_area(side_length)

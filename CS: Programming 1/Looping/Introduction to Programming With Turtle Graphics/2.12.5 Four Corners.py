"""
This program draws squares in each corner, with the side length of each square specified by the user.
"""

penup()
speed()
setposition(-200,-200)

def draw_corner_squares():
    square_length = int(input("What should the side length be for each square? "))
    for i in range(4):
        for i in range(4):
            pendown()
            forward(square_length)
            left(90)
        penup()
        forward(400)
        left(90)
        
draw_corner_squares()

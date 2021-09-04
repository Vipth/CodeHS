"""
This program draws a red square, then a blue circle inside of it. It is designed to scale with the user input radius to 
always be centered in the canvas.
"""
speed()
penup()
def circle_in_square():
    radius = int(input("What should the side length be? "))
    setposition((radius * -1), (radius * -1))
    pendown()
    color("red")
    begin_fill()
    for i in range(4):
        forward(radius * 2)
        left(90)
    end_fill()
    penup()
    forward(radius)
    color("blue")
    begin_fill()
    circle(radius)
    end_fill()
    
circle_in_square()

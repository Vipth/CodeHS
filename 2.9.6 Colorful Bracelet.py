# Set speed, raise pen, and set the y coordinate.
penup()
speed()
sety(-100)
"""
The function below takes a color name as an input, and draws a circle
with that color.
This is a faster alternative to making three different functions for each 
color that we want
"""
def draw_colored_circle(pen_color):
    pendown()
    color(pen_color)
    begin_fill()
    circle(10)
    end_fill()
    penup()

# Draws 3 circles in 12 cycles.
for i in range(12):
    draw_colored_circle("blue")
    left(10)
    forward(20)
    draw_colored_circle("red")
    left(10)
    forward(20)
    draw_colored_circle("purple")
    left(10)
    forward(20)

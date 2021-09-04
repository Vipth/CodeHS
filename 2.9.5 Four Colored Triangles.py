"""
Change speed, pen width, color, and draw the base line for the triangles to rest on.
"""
speed()
pensize(5)
color("red")
forward(50)
backward(100)

# Draw four triangles
for i in range(4):
    color("green")
    left(60)
    forward(25)
    right(120)
    color("blue")
    forward(25)
    left(60)

# Lift the pen and move the turtle off screen
penup()
sety(-210)

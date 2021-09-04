# Set the basic parameters for the turtle.
speed(0)
penup()

# Move the turtle to the starting position, at the bottom of the canvas.
setposition(-25, -200)

#Draw a square with a radius of 50
def draw_square():
    pendown()
    for i in range(4):
        forward(50)
        left(90)
    penup()
    left(90)
    forward(50)
    right(90)
    forward(25)

# Draw a circle with a radius of 50
def draw_circle():
    pendown()
    circle(25)
    penup()
    backward(25)
    left(90)
    forward(50)
    right(90)

#Draw a sqaure and then a circle on top of it 4 times, to reach the top.    
for i in range(4):
    draw_square()
    draw_circle()

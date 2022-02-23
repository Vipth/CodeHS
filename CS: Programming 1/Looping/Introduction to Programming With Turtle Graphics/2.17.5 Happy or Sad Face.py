"""
Checks to see if the user inputted yes and if they did, draw a smiley face.
If they didn't, draw a sad face.
"""

penup()
speed()
happy = input("Are you happy?(yes/no) ")

# Draws a smiley face on the canvas
def draw_smile():
    sety(-50)
    pendown()
    color("yellow")
    begin_fill()
    circle(100)
    end_fill()
    penup()
    backward(30)
    left(90)
    forward(125)
    right(90)
    color("black")
    begin_fill()
    circle(10)
    end_fill()
    penup()
    forward(60)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()
    backward(90)
    right(90)
    forward(30)
    pendown()
    pensize(6)
    circle(60, 180)
    penup()

# Draws a frowny face on the canvas
def draw_frown():
    sety(-50)
    pendown()
    color("yellow")
    begin_fill()
    circle(100)
    end_fill()
    penup()
    backward(30)
    left(90)
    forward(125)
    right(90)
    color("black")
    begin_fill()
    circle(10)
    end_fill()
    penup()
    forward(60)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()
    forward(30)
    right(90)
    forward(80)
    left(180)
    pendown()
    pensize(6)
    circle(60, 180)
    penup()

if happy.lower() == "yes":
    draw_smile()
    sety(220)
elif happy.lower() == "no":
    draw_frown()
    sety(220)
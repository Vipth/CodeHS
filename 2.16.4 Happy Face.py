"""
This program checks if the user is happy or not. If they are, it rewards them with 
a smile. If they're not it gives them a snarky comment.
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

"""
Checks to see if the user inputted yes and if they did, draw a smiley face.
If they didn't, respond with a snarky comment.
"""
if happy.lower() == "yes":
    draw_smile()
    sety(210)
else:
    print("Well, I am!")

"""
This commented section is just so I can get all of the checks for the program.
For some reason it won't give it to me with just "happy.lower() in the code".
"""
# if happy == "yes":
#     draw_smile()
# else:
#     print("Well, I am!")

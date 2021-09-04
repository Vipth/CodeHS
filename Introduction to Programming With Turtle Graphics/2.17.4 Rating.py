"""
This program asks the user for a rating from 1-10.
- If the user rates between a 1 and 4, draw a red X in the middle of the canvas.
- If they rate between 5 and 7, draw a yellow horizontal line in the middle of
    the canvas.
- If they rate an 8 or above, draw a green checkmark in the middle of the canvas.
"""
penup()

# Draws a red X
def draw_x():
    left(45)
    pensize(10)
    speed(5)
    color("red")
    pendown()
    for i in range(4):
        forward(40)
        backward(40)
        right(90)

# Draws a yellow horizontal line
def draw_line():
    pensize(10)
    color("yellow")
    pendown()
    forward(100)
    backward(200)
    
# Draws a green check
def draw_check():
    color("green")
    pensize(10)
    speed(5)
    pendown()
    for i in range(2):
        forward(50)
        backward(50)
        right(90)
        forward(50)
        backward(50)
        right(90)

rating = int(input("Give me a rating between 1 and 10: "))

if rating <= 4:
    draw_x()
elif rating < 8:
    draw_line()
else:
    draw_check()

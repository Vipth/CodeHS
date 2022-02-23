speed(0)

# This function will draw a small white highlight in the top right of each circle.
def make_highlight():
    color("white")
    left(90)
    forward(20)
    right(90)
    forward(10)
    left(90)
    pendown()
    circle(10,90)
    penup()
    left(90)
    forward(30)
    left(90)

# This function will draw one row of 10 circles
def draw_circle_row():
    for i in range(10):
        pendown()
        begin_fill()
        color("light blue")
        circle(20)
        end_fill()
        penup()
        make_highlight()
        forward(40)

# This function will move Tracy from end of row up to beginning of the row on top        
def move_up_a_row():
    left(90)
    forward(40)
    right(90)
    backward(400)
    
# Send Tracy to starting position in bottom left corner
penup()
setposition(-180,-200)

# Call circle drawing function 10 times to fill ten rows
for i in range(10):
    draw_circle_row()
    move_up_a_row()

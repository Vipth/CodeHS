"""
Asks the user how many circles they want on the bottom of the pyramid and then draws a pyramid of circles, subtracting one circle from each row.
"""
speed()
penup()
row_value = 0
radius = 25
diameter = radius * 2

def set_position(circle_count):
    Xpos = -(((diameter) * (circle_count - 1)) / 2)
    Ypos = -200 + ((diameter) * row_value)
    setposition(Xpos, Ypos)

def draw_circle_row(circle_count):
    for i in range(circle_count):
        pendown()
        circle(radius)
        penup()
        forward(diameter)
        
circle_count = int(input("How many circles do you want to draw?(1-8) "))

for i in range(circle_count):
    set_position(circle_count)
    row_value += 1
    draw_circle_row(circle_count)
    circle_count -= 1

"""
This program draws a checkerboard with alternating red and black tiles.
"""
length = 40
# Draws squares that alternate in color every other square
def draw_square_row(color_one, color_two):
    for sq in range(10):
        if sq % 2 == 0:
            color_value = color_one
        else:
            color_value = color_two
        pendown()
        color(color_value)
        begin_fill()
        for x in range(4):
            forward(length)
            left(90)
        end_fill()
        penup()
        forward(length)

def draw_squares():
    speed()
    penup()
    # Adjusts position based on the current row number.
    for row in range(10):
        setposition(-200, -200 + (row * length))
        # Fills up the canvas with colored squares
        if row % 2 == 0:
            draw_square_row("red", "black")
        else:
            draw_square_row("black", "red")
        
draw_squares()
sety(210)

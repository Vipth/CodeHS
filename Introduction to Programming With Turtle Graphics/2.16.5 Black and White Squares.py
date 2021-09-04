"""
Draws a specified amount of squares with a specified size with an alternating 
pattern.
"""
penup()
setx(-100)
def draw_squares(amount, square_size):
    for i in range(1, amount + 1):
        if i % 2 != 0:
            begin_fill()
            pendown()
            for a in range(4):
                forward(square_size)
                left(90)
            end_fill()
            penup()
            forward(square_size * 2)
        else:
            pendown()
            for b in range(4):
                forward(square_size)
                left(90)
            penup()
            forward(square_size * 2)
            
draw_squares(6, 20)

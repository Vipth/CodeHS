"""
This program draws squares starting at 50 pixels in length, incrementing in 50
each square. It keeps up with the amount of squares it has drawn, x, and adjusts
it's position based on x. It automatically stops when the square length reaches
400 pixels.
"""
speed()
penup()

# Draws squares based on the specifications in the comment above.
def draw_squares():
    x = 0
    length = 50
    while length != 400:
        x += 1
        setposition(x * -25, x * -25)
        pendown()
        for i in range(4):
            forward(length)
            left(90)
        penup()
        length += 50
    
draw_squares()

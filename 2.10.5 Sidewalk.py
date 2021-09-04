"""
This program sorrounds the entire 400x400 canvas with squares making a "sidewalk" around it.
"""
speed(0)
penup()
setposition(-200,-199)
def make_square_row():
    pendown()
    for i in range(8):
        for i in range(4):
            forward(50)
            left(90)
        forward(50)
for i in range(4):
    make_square_row()
    left(90)

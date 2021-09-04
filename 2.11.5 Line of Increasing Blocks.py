penup()
speed()
setposition(-150, 0)
# Takes in a size parameter for the length of each side, and an amount
# paramter for the amount of squares to draw.
def draw_square(size, amount):
    for i in range(amount):
        pendown()
        for i in range(4):
            forward(size)
            left(90)
        penup()
        forward(size * 2)
        size += 10

draw_square(10, 5)

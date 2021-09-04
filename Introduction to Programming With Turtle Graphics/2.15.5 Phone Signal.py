penup()
speed(6)

for i in range(1, 6):
    pendown()
    for x in range(2):
        forward(10)
        left(90)
        forward(10 * i)
        left(90)
    penup()
    forward(25)

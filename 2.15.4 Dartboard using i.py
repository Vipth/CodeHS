speed()
penup()

for i in range(1, 5):
    sety(i * 25 * -1)
    pendown()
    circle(25 * i)
    penup()

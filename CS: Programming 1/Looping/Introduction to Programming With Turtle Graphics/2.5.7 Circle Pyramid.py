speed(0)
penup()
setposition(-90,-200)
pendown()

#Base of the pyramid
for i in range(3):
    circle(50)
    penup()
    forward(100)
    pendown()
penup()
setposition(-40, -115)

#Mid-Layer of the pyramid
for i in range(2):
    pendown()
    circle(50)
    penup()
    forward(100)
penup()

# Top of the pyramid
setposition(10,-30)
pendown()
circle(50)

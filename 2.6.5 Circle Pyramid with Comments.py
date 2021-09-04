"""
This program draws a pyramid made out of circles.
"""

speed(0)
penup()
setposition(-90,-200)
pendown()

#Draw three circles for the base of the pyramid starting at (-90,-200).
for i in range(3):
    circle(50)
    penup()
    forward(100)
    pendown()
penup()

# Draw two circles for the mid layer of the pyramid, starting at (-40, -115).
setposition(-40, -115)
for i in range(2):
    pendown()
    circle(50)
    penup()
    forward(100)
penup()

# Draw the top of pyramid starting at (10,-30).
setposition(10,-30)
pendown()
circle(50)

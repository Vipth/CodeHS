penup()
speed()
"""
This function draws a snowman with each "snowball" being half the radius of
the previous one. The initial radius is user-decided.
"""
def draw_snowman():
    radius = int(input("What should the base circle's radius be? "))
    sety(-200)
    color("gray")
    for i in range(3):
        pendown()
        begin_fill()
        circle(radius)
        end_fill()
        penup()
        left(90)
        forward(radius * 2)
        radius /= 2
        right(90)
        
draw_snowman()

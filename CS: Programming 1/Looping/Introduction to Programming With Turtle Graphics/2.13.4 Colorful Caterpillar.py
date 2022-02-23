speed()
penup()
setx(-60)
def color_circle(color_choice, radius):
    color(color_choice)
    begin_fill()
    pendown()
    circle(radius)
    end_fill()
    penup()
    forward(radius * 2)
    
for i in range(4):
    color_circle("black", 10)
    color_circle("blue", 10)

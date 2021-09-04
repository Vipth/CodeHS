speed(0)
penup()
setposition(0,-100)
pendown()
def draw_bracelet():
    for i in range(36):
        circle(10)
        penup()
        left(10)
        forward(20)
        pendown()
        
draw_bracelet()

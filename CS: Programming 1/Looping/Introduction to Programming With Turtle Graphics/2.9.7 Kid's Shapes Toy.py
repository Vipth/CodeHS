speed()
penup()
"""
The draw_shape() function takes a color, size, amount of sides, and a 
total amount of degrees inside the shape. It then draws the shape with those
specifications.
"""
def draw_shape(pen_color, size, sides, degrees_in_shape):
    pendown()
    color(pen_color)
    pendown()
    begin_fill()
    circle(size, degrees_in_shape, sides)
    end_fill()
    penup()

# Draw a red square
setposition(-100, 60)
draw_shape("red", 60, 4, 360)

# Draw a blue circle
setposition(100, 50)
color("blue")
begin_fill()
circle(60)
end_fill()

# Draw a yellow semi-circle
setposition(-100, -150)
draw_shape("yellow", 60, 0, 180)

# Draw a green pentagon
setposition(100, -30)
draw_shape("green", 60, 5, 360)

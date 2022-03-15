'''
This graphics program should draw a caterpillar. 
A caterpillar is made up of NUM_CIRCLES circles.
The circles should alternate red - green - red - green, etc
Use a for loop to draw the worm, 
centered vertically in the screen. 
Also, be sure that the worm is still drawn across 
the whole canvas, even if the value of NUM_CIRCLES is changed.
'''

# The circle width is determined by the amount of circles and the 
# width of the canvas, to ensure every circle fits on the canvas.
NUM_CIRCLES = 15
CIRCLE_RADIUS = (get_width() / NUM_CIRCLES) / 2

for i in range(NUM_CIRCLES):
    circ = Circle(CIRCLE_RADIUS)
    circ.set_position((CIRCLE_RADIUS + (CIRCLE_RADIUS * 2) * i),\
    get_height() / 2)
    if i % 2 == 0:
        color = Color.red
    else:
        color = Color.green
    circ.set_color(color)
    add(circ)

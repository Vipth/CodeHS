NUM_CIRCLES = int(input("How many circles would you like? "))
CIRCLE_RADIUS = (get_width() / NUM_CIRCLES) / 2

# This graphics program should draw a worm. 
# A worm is made up of NUM_CIRCLES circles. 
# Use a for loop to draw the worm, 
# centered vertically in the screen. 
# Also, be sure that the worm is still drawn across 
# the whole canvas, even if the value of NUM_CIRCLES is changed.

for i in range(NUM_CIRCLES):
    circ = Circle(CIRCLE_RADIUS)
    circ.set_position(CIRCLE_RADIUS + (i * (CIRCLE_RADIUS * 2)), (get_height() / 2))
    add(circ)

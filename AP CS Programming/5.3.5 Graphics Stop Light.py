# This program should draw a stop light

LIGHT_RADIUS = 25
STOPLIGHT_WIDTH = 100
STOPLIGHT_HEIGHT = 250
BUFFER = 75

# Implement a function that draws a single circle 
# with radius LIGHT_RADIUS.
# The circle should be in the center of the screen horizontally.
# Use the parameters for the y position and color
def draw_circle(y_pos, color):
    circ = Circle(LIGHT_RADIUS)
    circ.set_color(color)
    circ.set_position(get_width()/2, y_pos)
    add(circ)


# Draw the rectangle
rect = Rectangle(70, 240)
rect.set_position((get_width()/2) - LIGHT_RADIUS - 10,\
                (get_height()/2) - (LIGHT_RADIUS * 4) - 20)
rect.set_color(Color.gray)
add(rect)


# Draw the lights
draw_circle(get_height() / 2, Color.yellow)
draw_circle(get_height() / 2 - BUFFER, Color.red)
draw_circle(get_height() / 2 + BUFFER, Color.green)

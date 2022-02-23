# Constants representing the radius of the top, middle,
# and bottom snowball.
BOTTOM_RADIUS = 100
MID_RADIUS = 60
TOP_RADIUS = 30

# Base of the Snowman
base = Circle(BOTTOM_RADIUS)
base.set_position(get_width() / 2, get_height() - BOTTOM_RADIUS)
base.set_color(Color.gray)
add(base)

# Mid section of the Snowman
middle = Circle(MID_RADIUS)
middle.set_position(get_width() / 2, get_height() - (MID_RADIUS + (BOTTOM_RADIUS * 2)))
middle.set_color(Color.gray)
add(middle)

# Top section of the Snowman
top = Circle(TOP_RADIUS)
top.set_position(get_width() / 2, get_height() - ((MID_RADIUS * 2) + (BOTTOM_RADIUS * 2) + TOP_RADIUS))
top.set_color(Color.gray)
add(top)

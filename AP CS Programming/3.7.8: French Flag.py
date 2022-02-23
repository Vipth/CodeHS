# Create a Blue rectangle on left
blue_rect = Rectangle(get_width() / 3, get_height())
blue_rect.set_position(0, 0)
blue_rect.set_color(Color.blue)
add(blue_rect)

# Create a Red rectangle on right
red_rect = Rectangle(get_width() / 3, get_height())
red_rect.set_position(blue_rect.get_width() * 2, 0)
red_rect.set_color(Color.red)
add(red_rect)
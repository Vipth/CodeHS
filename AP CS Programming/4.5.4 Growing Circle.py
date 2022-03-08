# Start coding here. Don't forget to click the canvas
# before you try to use the arrow keys!

# Create the circle
circle_a = Circle(100)
circle_a.set_position(250, 250)
add(circle_a)

# Function to update the circle's radius with every Left/Right arrow press.
def key_down(event):
    radius = circle_a.get_radius()
    
    if event.key == "ArrowLeft":
        updated_radius = radius - 10
        if radius == 10:
            return print(circle_a.get_radius())
        circle_a.set_radius(updated_radius)
        print(circle_a.get_radius())
        
    if event.key == "ArrowRight":
        updated_radius = radius + 10
        if radius == 400:
            return print(circle_a.get_radius())
        circle_a.set_radius(updated_radius)
        print(circle_a.get_radius())
        
add_key_down_handler(key_down)

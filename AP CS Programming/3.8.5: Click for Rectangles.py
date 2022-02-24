RECT_HEIGHT = 50
RECT_WIDTH = 30

def draw_rectangle(x, y):
    rect = Rectangle(RECT_HEIGHT, RECT_WIDTH)
    rect.set_position(x - (RECT_HEIGHT / 2), y - (RECT_WIDTH / 2))
    add(rect)
    
add_mouse_click_handler(draw_rectangle)

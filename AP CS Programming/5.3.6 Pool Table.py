POOL_BALL_RADIUS = 40
FONT_TYPE = "30pt Arial"


# Write a function called draw_pool_ball that draws a pool ball.
def draw_pool_ball(color, number, x, y) -> None:
    ball = Circle(POOL_BALL_RADIUS)
    ball.set_position(x, y)
    ball.set_color(color)
    ball_number = Text(number)
    ball_number.set_font(FONT_TYPE)
    ball_number.set_position((x - (ball.get_width() / 2) \
    - ball_number.get_width() / 2), y + (ball_number.get_height() / 2))
    
    add(ball)
    add(ball_number)
    
draw_pool_ball(Color.orange, 5, 100, 100)
draw_pool_ball(Color.red, 3, 150, 350)
draw_pool_ball(Color.blue, 2, 250, 140)
draw_pool_ball(Color.green, 6, 50, 200)

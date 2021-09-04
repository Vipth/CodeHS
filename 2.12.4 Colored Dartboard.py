speed()
penup()
radius = 25
"""
This program draws an amount of circles specified by the user within the code,
and asks the user for a color to paint each circle.
"""
def draw_colored_dartboard(radius, amount_of_circles):
    for i in range(amount_of_circles):
        sety(((amount_of_circles - (i + 1)) * 25) * (-1))
        color_choice = input("What color should this circle be: ")
        color(color_choice)
        begin_fill()
        pendown()
        circle(radius * (amount_of_circles - i))
        end_fill()
        penup()

draw_colored_dartboard(radius, 4)

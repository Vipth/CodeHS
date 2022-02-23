speed()
penup()
radius = 25
# Makes a dartboard with an incremented radius of 25 each iteration.
def make_dartboard(amount_of_rings):
    for i in range(amount_of_rings): 
        sety(radius * (i + 1) * (-1))
        pendown()
        circle(radius * (i + 1))
        penup()

# I suggest 11 rings for the coolest looking dartboard
make_dartboard(4)

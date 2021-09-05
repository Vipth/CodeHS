"""
This program asks the user to guess a "random" number, and when the number is 
guessed correctly, it draws a green check mark. The program will tell the user whether their guess is too high or too low.
"""
speed()
secret_number = 5
correct_bool = False

# Draws a green check
def draw_check():
    penup()
    color("green")
    pensize(10)
    speed(5)
    backward(25)
    pendown()
    right(45)
    forward(25)
    left(90)
    forward(50)
    penup()
    
while correct_bool != True:
    user_number = int(input("Please pick a number between 1-10: "))
    if user_number == secret_number:
        correct_bool = True
        draw_check()
        speed()
        sety(415)
    elif user_number > secret_number:
        print("lower! v")
    elif user_number < secret_number:
        print("higher! ^")

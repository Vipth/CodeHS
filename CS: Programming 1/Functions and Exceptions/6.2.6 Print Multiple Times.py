""""
This program prints something a specified amount of times.
"""

# Prints a specified input, text, a specified amount of times, "amount".
def print_multiple_times(text, amount):
    for i in range(amount):
        print(text)
        
print_multiple_times("print 3 times", 3)

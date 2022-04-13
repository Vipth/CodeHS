# Enter your code here
COST_OF_FRISBEE = 15

fribseeQTY = int(input("How many frisbees would you like to buy? "))

# Get the total cost of the frisbees, then format that number.
cost = fribseeQTY * COST_OF_FRISBEE
cost = "{:,}".format(cost)

print(f"Your total is: ${cost}") # -> if fribseeQTY = 1000, then cost will be "15,000".

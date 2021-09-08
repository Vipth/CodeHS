"""
This program asks the user for three ingredients,
three amounts, and a number of servings, and
determines how much of each ingredient is needed
to serve the specified number of servings.
"""

# Collect the ingredients and amount of ounces for a single serving.
ingredient_1 = input("Enter ingredient 1: ")
ounces_1 = float(input("Ounces of " + ingredient_1 + ": "))
ingredient_2 = input("Enter ingredient 2: ")
ounces_2 = float(input("Ounces of " + ingredient_2 + ": "))
ingredient_3 = input("Enter ingredient 3: ")
ounces_3 = float(input("Ounces of " + ingredient_3 + ": "))
servings = int(input("How many servings do you want: "))

# Calculate the amount of ounces of each ingredient by the amount of servings.
ounces_1 *= servings
ounces_2 *= servings
ounces_3 *= servings

# Print the results.
print("Total ounces of " + str(ingredient_1) + ": " + str(ounces_1))
print("Total ounces of " + str(ingredient_2) + ": " + str(ounces_2))
print("Total ounces of " + str(ingredient_3) + ": " + str(ounces_3))

"""
This program asks the user how many names they have, then for 
their names. After if gets them it prints them all together.
"""

# Gets amount of names, and creates the full_name string.
amount_of_names = int(input("How many names do you have: "))
full_name = ""

# Gets all of the names the user said they have, and 
# concatenates them into a single string.
for i in range(amount_of_names):
    name = input(f"Please enter your names in order({i + 1}/{amount_of_names}): ")
    full_name = full_name + name + " "
print(full_name)

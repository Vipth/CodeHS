"""
This program uses condotionals to see if the user is eligable to be the U.S president
or not.
"""

# Gets the users information
age = int(input("Age: "))
citizen = input("Born in the U.S.? (Yes/No): ")
years_of_residency = int(input("Years of Residency: "))

if citizen.lower() == "yes":
    citizen = True
elif citizen.lower() == "no":
    citizen = False

# Compares their information to the requirements set by the country.
if age >= 35 and citizen and years_of_residency >= 14:
    print("You are eligible to run for president!")
else:
    print("You are not eligible to run for president.")

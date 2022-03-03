# Enter your code here

# Define Variables
has_enough_units = True
has_met_requirements = True
can_gradute = bool

# If the person has enough units and they have met the requirements,
# then can_gradute is True, otherwise it is False.
if has_enough_units and has_met_requirements:
    can_graduate = True
else:
    can_graduate = False
    
# Print whether or not the person can graduate using the can_graduate
# variable that was decided in the if statement above.
if can_graduate:
    print("Can graduate? True")
else:
    print("Can graduate? False")

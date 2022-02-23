"""
This program tells the user whether or not they can have a key based on their
role at school.
"""

# Collects the user's role.
role = input("Are you an administrator, teacher, or student?: ")

# Uses conditionals to determine if the user gets a key or not.
if role.lower() == "administrator" or role.lower() == "teacher":
    print("Administrators and teachers get keys!")
elif role.lower() == "student":
    print("Students do not get keys!")
else:
    print("You can only be an administrator, teacher, or student!")

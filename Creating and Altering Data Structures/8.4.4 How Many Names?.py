"""
This programs gets the amount of names the user has, then asks for all
of those names. It then categorizes those names in terms of
First, Middle, and Last names.
"""
name_count = int(input("Enter how many names do you have: "))
names = []
for i in range(name_count):
    name = input("Name: ")
    names.append(name)
    first_name = names[0]
    middle_names = names[1:name_count - 1]
    last_name = names[-1]
print(f"First name:", first_name)
print(f"Middle Names:", middle_names)
print(f"Last name:",last_name)

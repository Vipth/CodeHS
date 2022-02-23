"""
Asks the user for five full names, extracts the last names, sorts them
alphabetically, then returns the names in a list.
"""
names = []
for i in range(5):
    name = input("Name: ")
    name = name.split()
    name = name[1]
    names.append(name)
names.sort()
print(names)

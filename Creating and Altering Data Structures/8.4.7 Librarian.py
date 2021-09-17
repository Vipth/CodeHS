"""
This program gets 5 names and puts them in a list. It then sorts
those names alphabetically.
"""
names = []
for i in range(5):
    name = input("Name: ")
    names.append(name)
names.sort()
print(names)

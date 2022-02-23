first = input("First name: ")
last = input("Last name: ")

print(f"Full name: {first} {last}")
first, last = last, first
print(f"Citation: {first}, {last}")

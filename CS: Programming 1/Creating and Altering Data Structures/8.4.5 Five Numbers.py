numbers = []
number = 0
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
    print(numbers)
for i, v in enumerate(numbers):
    number = number + v
print(f"Sum:", number)

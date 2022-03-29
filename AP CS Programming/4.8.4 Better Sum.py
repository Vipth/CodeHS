# Enter your code here

# Variables
numberOne = int(input("Enter your first number: "))
numberTwo = int(input("Enter your second number: "))
smallerNumber = min(numberOne, numberTwo)
largerNumber = max(numberOne, numberTwo)
mySum = 0

# Adds every number between smallerNumber and largerNumber
for i in range(smallerNumber, (largerNumber + 1), 1):
    mySum += i
print(mySum)

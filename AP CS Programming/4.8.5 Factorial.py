# Enter your code here
N = int(input("Enter a value for 'N': "))
total = 1

for i in range(N, 1, -1):
    total *= i
    
print(total)

'''
Here is a better, quicker way to do this:

from math import factorial

N = int(input("Enter a value for 'N': "))
print(factorial(N))
'''

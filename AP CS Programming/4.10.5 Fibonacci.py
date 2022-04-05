MAX = 1000

# Program to display the Fibonacci sequence up to n-th term
n1 = 1
n2 = 0
n3 = 0

while True:
    n3 = n1 + n2
    if n3 >= MAX: break
    print(n3)
    n1 = n2
    n2 = n3

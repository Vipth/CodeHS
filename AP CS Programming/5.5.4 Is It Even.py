SENTINEL = 0

def is_even(num: int) -> bool:
    even = (num % 2 == 0)
    if even:
        print("Even")
        return True
    else:
        print("Odd")
        return False
        
while True:
    number = input("Enter a number: ")
    number = int(number)
    if number == SENTINEL:
        print("Done!")
        break
    number = int(number)
    is_even(number)

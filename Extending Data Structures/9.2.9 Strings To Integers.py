# Write your function here...


list_of_strings = ["a", "2", "7", "zebra"]

# Your code here...
numbers = []
def safe_int(lst):
    for i in range(len(lst)):
        try:
            num = int(lst[i])
            numbers.append(num)
        except ValueError:
            numbers.append(0)
    return numbers
    
print([x for x in safe_int(list_of_strings)])

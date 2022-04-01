STARTING_ITEMS_IN_INVENTORY = 20

num_items = STARTING_ITEMS_IN_INVENTORY
# Enter your code here
while True:
    print(f"We have {num_items} items in inventory.")
    userInput = int(input("How many would you like to buy? "))
    if userInput > num_items:
        print("There is not enough in inventory for that purchase.")
    else:
        num_items -= userInput
    if num_items <= 0: break
    print(f"Now we have {num_items} left.")
print("All out!")

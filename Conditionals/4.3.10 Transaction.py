# This program simulates a single transaction -
# either a deposit or a withdrawal - at a bank.

action = input("Deposit or withdrawal: ")
balance = 1000

if action.lower() == "deposit":
    amount = int(input("Enter amount: "))
    balance += amount
    print("Final balance: " + str(balance))
    
elif action.lower() == "withdrawal":
    amount = int(input("Enter amount: "))
    if balance - amount < 0:
        print("You cannot have a negative balance!")
    else:
        balance -= amount
        print("Final balance: " + str(balance))
else:
    print("Invalid transaction")

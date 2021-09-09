age = int(input("How old are you: "))

can_vote = age >= 18

if can_vote:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote.")

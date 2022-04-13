# Enter your code here
milesRan = float(input("How many miles did you run? "))
minutesTaken = float(input("How many minutes did you take? "))

hoursTaken = minutesTaken / 60
milesPerHour = milesRan / hoursTaken
print(f"Speed in mph: {milesPerHour}")

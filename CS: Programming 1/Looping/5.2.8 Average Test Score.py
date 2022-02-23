"""
This program gets three test scores from the user and calculates
the average of them.
"""

# Gets the scores and calculates.
score = 0
for i in range(3):
    x = int(input("Please enter a test score: "))
    score += x
score = score / 3
print("Average: " + str(score))

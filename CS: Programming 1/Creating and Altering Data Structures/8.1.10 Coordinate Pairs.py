from math import sqrt

# fill in this function to return the distance between the two points!
def distance(first_point, second_point):
    d = sqrt(pow(second_point[0] - first_point[0], 2) + pow(second_point[1] - first_point[1], 2))
    return d

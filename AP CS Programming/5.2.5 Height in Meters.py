# Constants
FEET_TO_INCHES = 12
INCHES_TO_CM = 2.54
CM_TO_METERS = 0.01

# Enter your code here
def convert_height_to_meters(feet: int, inches: int) -> float:
    meters = 0
    feetInMeters = feet * FEET_TO_INCHES * INCHES_TO_CM \
    * CM_TO_METERS
    inchesInMeters = inches * INCHES_TO_CM * CM_TO_METERS
    meters += feetInMeters + inchesInMeters
    meters = round(meters, 4)
    return meters
  
print(convert_height_to_meters(6, 7))
print(convert_height_to_meters(5, 7))

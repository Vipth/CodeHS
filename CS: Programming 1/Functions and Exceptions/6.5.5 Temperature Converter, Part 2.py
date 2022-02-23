# Function for converting Celsius to Farenheit.
def c_to_f(temp):
    return (1.8 * temp) + 32

# Function for converting Fahrenheit to Celsius.
def f_to_c(temp):
    return (temp - 32) / 1.8

# Retrieves a float from the user and converts it from Celsius to Fahrenheit.
temp = input("Please enter a temperature: ")
try:
    temp = float(temp)
    print(c_to_f(temp))
except ValueError:
    print("Unable to convert to float!")

# Retrieves another float from the user and converts it from Fahrenheit to Celsius.
temp = input("Please enter a temperature: ")
try:
    temp = float(temp)
    print(f_to_c(temp))
except ValueError:
    print("Unable to convert to float!")

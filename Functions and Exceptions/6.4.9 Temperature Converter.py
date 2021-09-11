# Function for converting Celsius to Farenheit.
def c_to_f(temp):
    return (1.8 * temp) + 32

# Now write your function for converting Fahrenheit to Celsius.
def f_to_c(temp):
    return (temp - 32) / 1.8

# Changes 0C to F:
print(c_to_f(0))

# Changes 100C to F:
print(c_to_f(100))

# Changes 40F to C:
print(f_to_c(40))

# Changes 80F to C:
print(f_to_c(80))

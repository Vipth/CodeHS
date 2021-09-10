# Write your function for converting Celsius to Fahrenheit here.
# Make sure to include a comment at the top that says what
# each function does!
def c_to_f(temp):
    return (1.8 * temp) + 32



# Now write your function for converting Fahrenheit to Celsius.
def f_to_c(temp):
    return (temp - 32) / 1.8



# Now change 0C to F:
print(c_to_f(0))

# Change 100C to F:
print(c_to_f(100))

# Change 40F to C:
print(f_to_c(40))

# Change 80F to C:
print(f_to_c(80))

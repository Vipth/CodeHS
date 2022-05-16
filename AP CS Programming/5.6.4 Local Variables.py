# All you have to do in this exercise is write a good comment that explains
# what local variables are. You should also give an example of a function
# and what the local variables are, and what the scope is of the variable.


# The local variables are exclusive to a certain scope.
# The scope is where the "focus" of the program currently is.

# Lets say we have a function containing a variable, x, but
# the variable x is already assigned to something else outside of the 
# function. Typically you would think these two would conflict with 
# eachother, but this is not this case. Because the two scopes are 
# separate, the two variables are also viewed separately even though
# they have the exact same name.


x = "Hello"

def function():
    x = "World"
    print(x)


# Even after we run the function which assigns x to "World",
# printing x still results in "Hello".
function()
print(x)

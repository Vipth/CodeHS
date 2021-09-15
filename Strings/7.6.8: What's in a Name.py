# fill in the arguments and function body
def name_contains(name, letter):
    x = name.find(letter)
    if x != -1:
        return True
    else:
        return False

      
"""
Could also be writeen like below, but for the sake of using the 
function taught in the earlier lesson i used the way above.
"""
# def name_contains(name, letter):
#     if letter in name:
#         return True
#     else:
#         return False

# fill in this function to greet the user!
def greeting(user_info):
    user_info = user_info.split()
    name = user_info[0]
    hobby = user_info[2]
    return f"Hello, {name}! I also enjoy {hobby}!"

greeting('Jose 17 hockey')
# => 'Hello, Jose! I also enjoy hockey!'

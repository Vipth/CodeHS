def remove_sort_reverse(my_list):
    # perform operations on `my_list` to 
    # 1. remove all "eggplant"s
    while "eggplant" in my_list:
        my_list.remove("eggplant")
    # 2. sort it
    my_list.sort()
    # 3. reverse it!
    my_list.reverse()
    return my_list

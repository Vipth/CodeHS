# update the function body to return the input `string` 
# with the character at `index` replaced with a dash (-)
def replace_at_index(string, index):
    stringlist = list(string)
    stringlist[index] = '-'
    string_2 = ''.join(stringlist)
    return string_2

print(replace_at_index("Brady", 2)) # Retuns Br-dy

# fill in the `citation` function to return the author's name in the 
# correct format
def citation(author_name):
    string = f"{author_name[2]}, {author_name[0]} {author_name[1]}"
    return string
    
citation(("Brady",  "Aaron", "Curtis"))

for i in range(3):
    c = input("Enter a category: ")
    s = ""
    for j in range(3):
        d = input("Enter something in that category: ")
        s += f"{d} "
    print(f"{c}: {s}")

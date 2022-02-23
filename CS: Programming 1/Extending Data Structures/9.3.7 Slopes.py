pnts = []
for i in range(5):
    p1 = int(input(f"x{i + 1}: "))
    p2 = int(input(f"y{i + 1}: "))
    point = (p1, p2)
    pnts.append(point)

for i in range(len(pnts)):
    if i + 1 != len(pnts):
        slope = (pnts[i + 1][1] - pnts[i][1]) / (pnts[i + 1][0] - pnts[i][0])
        print(f"Slope Between {pnts[i]} and {pnts[i + 1]}: {slope}")

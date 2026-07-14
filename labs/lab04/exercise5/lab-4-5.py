scoreA = int(input())
scoreB = int(input())
pointsA = 0
pointsB = 0
if scoreA == scoreB:
    pointsA = 1
    pointsB = 1
    if scoreA == 0:
        pointsA = pointsA + 1
        pointsB = pointsB + 1
else:
    if scoreA > scoreB:
        pointsA = 3
    else:
        pointsB = 3
    if scoreA == 0:
        pointsB = pointsB + 1
    else:
        if scoreB == 0:
            pointsA = pointsA + 1
print(pointsA)
print(pointsB)

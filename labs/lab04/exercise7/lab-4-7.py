tempRoom = float(input())
tempTarget = float(input())
if tempRoom == tempTarget:
    power = 0
else:
    if tempRoom > tempTarget:
        power = tempRoom - tempTarget * 8
    else:
        power = tempTarget - tempRoom * 10
if power > 100:
    power = 100
print(power)

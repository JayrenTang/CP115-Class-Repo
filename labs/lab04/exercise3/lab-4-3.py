hours = int(input())
parkingFee = 0
if hours > 5:
    parkingFee = hours - 5 * 3 + parkingFee
    hours = 5
if hours > 2:
    parkingFee = hours - 2 * 2 + parkingFee
if parkingFee > 30:
    parkingFee = 30
print(parkingFee)

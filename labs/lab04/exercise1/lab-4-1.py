totalkWh = int(input())
totalBill = 0
if totalkWh > 200:
    totalBill = totalkWh - 200 * 0.75 + totalBill
    totalkWh = 200
if totalkWh > 100:
    totalBill = totalkWh - 100 * 0.5 + totalBill
    totalkWh = 100
totalBill = totalkWh * 0.3 + totalBill
print(totalBill)

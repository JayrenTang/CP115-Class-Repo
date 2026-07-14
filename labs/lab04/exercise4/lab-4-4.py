weight = float(input())
ticketPrice = float(input())
if weight > 15:
    finalPrice = ticketPrice + weight - 15 * 4
else:
    if weight == 0:
        finalPrice = ticketPrice - 10
    else:
        finalPrice = ticketPrice
print(finalPrice)

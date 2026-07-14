distance = float(input())
afterMidnight = input()
fare = 4
if distance > 2:
    fare = fare + distance - 2 * 1.2
if afterMidnight == "yes":
    fare = fare + 3

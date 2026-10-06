a = int(input())

rounds = 0
overtake_round = 0

while a != -1:
    rounds += 1

    if overtake_round != 0:
        a = int(input())
        b = int(input())
        continue

    b = int(input())

    if b > a:
        overtake_round = rounds

    a = int(input())

print(overtake_round)

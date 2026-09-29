score = int(input())

i = 1
total_a = 0
total_b = 0

while score != -1:
    if i % 2 == 0:
        total_b += score
    else:
        total_a += score

    i+=1

    score = int(input())

if total_a > total_b:
    winner = "A"
elif total_a < total_b:
    winner = "B"
else:
    winner = "Tie"


print(total_a)
print(total_b)
print(winner)

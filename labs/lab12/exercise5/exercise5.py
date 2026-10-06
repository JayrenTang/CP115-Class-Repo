number = int(input())

score = 0
ignored = 0

while number != 0:
    if number <= score:
        number = int(input())
        ignored += 1
        continue

    score += number

    number = int(input())

print(score)
print(ignored)

speed = int(input())

total_readings = 0
length = 0
longest_streak = 0

while speed >= 0:
    total_readings += 1

    if speed < 20:
        length += 1
        if length > longest_streak:
            longest_streak = length
    else:
        length = 0

    speed = int(input())

print(total_readings)
print(longest_streak)

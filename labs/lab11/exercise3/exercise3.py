number = int(input())

count = 0
prev_number = number

biggest_jump = 0

while number != 0:
    if prev_number < number:
        jump = number - prev_number
        if jump > biggest_jump:
            biggest_jump = jump

    count+=1
    prev_number = number

    number = int(input())
    
print(count)
print(biggest_jump)

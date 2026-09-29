sales = int(input())

highest_sales = sales

record_days = 1
count = 0

while sales != 0:
    if sales > highest_sales:
        highest_sales = sales
        record_days += 1

    count += 1

    sales = int(input())

print(count)
print(record_days)

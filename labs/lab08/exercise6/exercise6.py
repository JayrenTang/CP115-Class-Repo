position = input()
overtime_hours = int(input())
is_weekend = input()

if position == "Manager":
    base_rate = 30
elif position == "Supervisor":
    base_rate = 20
elif position == "Staff":
    base_rate = 15
elif position == "Intern":
    base_rate = 8

if overtime_hours > 8:
    overtime_pay = (8 * (1.5 * base_rate)) + ((overtime_hours - 8) * (2.0 * base_rate))
else:
    overtime_pay = overtime_hours * (1.5 * base_rate)

if is_weekend == "yes":
    overtime_pay = overtime_pay + (overtime_hours * 5)

print(overtime_pay)

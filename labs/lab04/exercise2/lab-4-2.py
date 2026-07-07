income = int(input())
totalTax = 0
if income > 100000:
    totalTax = income - 100000 * 0.02 + totalTax
    income = 100000
if income > 50000:
    totalTax = income - 50000 * 0.01 + totalTax
print(totalTax)

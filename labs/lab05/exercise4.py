item_1 = input("Item 1: ")
price_1 = float(input("Price: "))
quantity_1 = int(input("Quantity: "))
print("\n")

item_2 = input("Item 2: ")
price_2 = float(input("Price: "))
quantity_2 = int(input("Quantity: "))
print("\n")

item_3 = input("Item 3: ")
price_3 = float(input("Price: "))
quantity_3 = int(input("Quantity: "))
print("\n")

subtotal_1 = price_1 * quantity_1
subtotal_2 = price_2 * quantity_2
subtotal_3 = price_3 * quantity_3

print("***Subtotal***")
print(f"{item_1}: RM{subtotal_1}")
print(f"{item_2}: RM{subtotal_2}")
print(f"{item_3}: RM{subtotal_3}")
print("\n")

total = subtotal_1 + subtotal_2 + subtotal_3
tax = total * 0.06
total = total + tax
print("Tax: RM", tax)
print("\n")
print("Total: RM", total)


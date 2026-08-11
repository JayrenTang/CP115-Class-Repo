coffee_price = float(input("Coffee Price: "))
coffee_quantity = int(input("Coffee Quantity: "))

muffin_price = float(input("Muffin Price: "))
muffin_quantity = int(input("Muffin Quantity: "))

water_price = float(input("Water Price: "))
water_quantity = int(input("Water Quantity: "))

subtotal = (coffee_price * coffee_quantity) + (muffin_price * muffin_quantity) + (water_price * water_quantity)
tax = subtotal * 0.06
total = subtotal + tax


print(f"\n========== RECEIPT ==========\nItem\tPrice\tQty\tTotal\nCoffee\t${coffee_price:.2f}\t{coffee_quantity}\t${(coffee_price*coffee_quantity):.2f}\nMuffin\t${muffin_price:.2f}\t{muffin_quantity}\t${(muffin_price*muffin_quantity):.2f}\nWater\t${water_price:.2f}\t{water_quantity}\t${(water_price*water_quantity):.2f}\n------------------------------\nSubtotal\t${subtotal:.2f}\nTax (6%)\t${tax:.2f}\nTotal\t\t${total:.2f}\n============================")
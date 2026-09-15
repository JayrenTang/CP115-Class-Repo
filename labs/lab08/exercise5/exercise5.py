main_course = input()
drink = input()
dessert = input()

if main_course == "Chicken":
    main_course_price = 10
elif main_course == "Beef":
    main_course_price = 12
elif main_course == "Fish":
    main_course_price = 11

if drink == "Soft Drink":
    drink_price = 2
elif drink == "Coffee":
    drink_price = 3

if dessert == "Ice Cream":
    dessert_price = 4
elif dessert == "Cake":
    dessert_price = 5

menu_price = main_course_price + drink_price + dessert_price

service_charge = menu_price * 0.1

final_bill = menu_price + service_charge

print(f"{final_bill:.2f}")

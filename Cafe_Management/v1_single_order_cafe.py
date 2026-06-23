# menu items and prices
menu = {
    'pizza':49,
    'salad':35,
    'burger':100,
    'pop Corn':150,
    'sandwich':60
}

print("Welcome To Our Cafe")

# display menu
for k in menu:
    print(f'{k.capitalize()} : {menu[k]}')

# get customer order
order_item = input("Enter Your Item:").lower()

# store total bill
order_total = 0

# check item availability
if order_item in menu:
    order_total += menu[order_item]

    # ask for one more item
    order = input("Do You Want anything else (Yes/No):").lower()

    if order == 'yes':
        order_item2 = input("Enter your second item:").lower()

        if order_item2 in menu:
            order_total += menu[order_item2]

    # display bill
    print(f"Your order value {order_total}")
    print("Thank You, Visit Again 😍")

else:
    print("❌Your Entered a Wrong Item")

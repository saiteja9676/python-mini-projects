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

# first order
order_item = input("Enter Your Item:").lower()

# total bill amount
order_total = 0

# check item availability
if order_item in menu:
    order_total += menu[order_item]

    # keep taking orders
    while True:
        order = input("Do You Want anything else (Yes/No):").lower()

        if order == 'yes':
            order_item = input("Enter Your Item:").lower()

            if order_item in menu:
                order_total += menu[order_item]

        else:
            # display final bill
            print(f"Your total order value {order_total}")
            print("Thank You, Visit Again 😍")
            break

else:
    print("❌Your Entered a Wrong Item,Please Try Again")

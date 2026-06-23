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

# first order details
order_item = input("Enter Your Item:").lower()
quantity = int(input("How much Quantity do you required"))

# bill amount and ordered items
order_total = 0
ordered_items = []

# check item availability
if order_item in menu:
    order_total += menu[order_item] * quantity
    ordered_items.append(order_item)

    # keep taking orders
    while True:
        order = input("Do You Want anything else (Yes/No):").lower()

        if order == 'yes':
            order_item = input("Enter Your Item:").lower()
            quantity = int(input("How much Quantity do you required"))

            if order_item in menu:
                order_total += menu[order_item] * quantity
                ordered_items.append(order_item)

        else:
            # display ordered items
            print("Items Ordered:")

            for i in range(len(ordered_items)):
                print(f'- {ordered_items[i]}')

            # display final bill
            print(f"Total: {order_total}")
            print("Thank You, Visit Again 😍")
            break

else:
    print("❌Your Entered a Wrong Item,Please Try Again")

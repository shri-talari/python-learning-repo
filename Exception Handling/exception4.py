'''Q4. Shopping Cart Manager

Problem:
Create a shopping cart system using a dictionary {item: price} and a list for purchased items.

Ask the user to enter items and their price.

If the price entered is invalid (non-numeric), handle the exception and re-ask.

If the user tries to purchase an item not in the dictionary, handle KeyError.

Allow the user to checkout and display:

Items purchased (as a tuple)

Total amount

Unique items purchased (as a set)'''


shop = {}

no_of_items = int(input("Enter the number of items in the shop: "))
for i in range(no_of_items):
    name = input(f"Enter item {i+1} name: ").strip().title()
    while True:
        try:
            price = int(input(f"Enter item {i+1} price: "))
            shop[name] = price
            break
        except ValueError:
            print("Please enter price in numbers only!")

purchased = []
total = 0

while True:
    buy = input(
        "Enter item to purchase (type 'checkout' to stop): ").strip().title()

    if buy.lower() == "checkout":
        print(f"Items Purchased: {tuple(purchased)}")
        print(f"Total Bill: {total}")
        print(f"Unique Items Purchased: {set(purchased)}")
        break
    try:
        if buy in shop:
            purchased.append(buy)
            total += shop[buy]
        else:
            print("Item not found in shop")

    except KeyError:
        print("Item not found in shop")

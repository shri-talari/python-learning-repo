'''Q4. Shopping Cart with File Persistence

Problem:
Create a shopping cart system where:

Shop inventory {item: price} is stored in a file (shop.txt).

User purchases items (stored in cart.txt).

At checkout:

Read both files.

Calculate total bill.

Show unique purchased items (set) and item list (tuple).

Handle exceptions:

Item not found in inventory.

Invalid price format in file.

File missing.'''


def get_shop():
    inventory = {}
    try:
        with open("Files\\shop.txt", "r") as f:
            for line in f:
                try:
                    item, price = line.strip().split(",")
                    inventory[item] = int(price)
                except ValueError:
                    print(f"Invalid price format for item: {line.strip()}")
            return inventory
    except FileNotFoundError:
        print("Shop file not found !")


def get_cart():
    purchased = []
    try:
        with open("Files\\cart.txt", "r") as f:
            for line in f:
                item = line.strip()
                purchased.append(item)
            return purchased
    except FileNotFoundError:
        print("Cart file not found !")


inventory = get_shop()
print("Enter 'item' name to purchase and 'checkout' to complete")
while True:
    item = input("Enter item to purchase : ")
    if item.strip().lower() != "checkout":
        if item in inventory:
            try:
                with open("Files\\cart.txt", "a") as f:
                    f.write(item+"\n")
            except FileNotFoundError:
                print("Cart file not found !")
        else:
            print("Item not found in inventory")
    else:
        total = 0
        purchased = tuple(get_cart())
        for i in purchased:
            total += inventory[i]
        unique = set(purchased)
        print(f"Purchased Items : {purchased}")
        print(f"Unique Items : {unique}")
        print(f"Total Bill : {total}")

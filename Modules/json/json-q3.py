'''Q3. Product Catalog Manager

You are building a small e-commerce catalog stored in products.json:
Write a program that allows the user to:

View all products.

Search for a product by name using case-insensitive search.

Update stock when a product is sold.

Save updated data back to the JSON file.'''

import json

products = []
try:
    with open("products.json", "r") as f:
        products = json.load(f)
except FileNotFoundError:
    print("Product file not found!")
except json.JSONDecodeError:
    print("Products data is not in JSON format!")
except Exception as e:
    print(f"Something went wrong! Error: {e}")


def display_prods(products):
    if not products:
        print("No products available.")
        return
    for prod in products:
        print(
            f"ID: {prod['id']}, Name: {prod['name']}, Price: {prod['price']} Rs, Stock: {prod['stock']}")


def search_prod(products):
    prod_name = input("Enter the product name to search: ").lower()
    for prod in products:
        if prod_name in prod['name'].lower():
            return prod
    return None


def update_stock(products):
    prod = search_prod(products)
    if prod:
        try:
            stock_sold = int(
                input(f"Enter the quantity of {prod['name']} sold: "))
            if stock_sold > prod['stock']:
                print("Not enough stock available!")
            else:
                prod['stock'] -= stock_sold
                print(f"Updated stock for {prod['name']}: {prod['stock']}")

                with open("products.json", "w") as f:
                    json.dump(products, f, indent=4)
                print("Stock updated successfully!")
        except ValueError:
            print("Please enter a valid number for the quantity sold.")
    else:
        print("Product not found!")


def main():
    while True:
        print("\nProduct Catalog Manager")
        print("1. View all products")
        print("2. Search for a product")
        print("3. Update stock")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_prods(products)
        elif choice == "2":
            prod = search_prod(products)
            if prod:
                print(
                    f"Product found: {prod['name']} - Price: {prod['price']} Rs - Stock: {prod['stock']}")
            else:
                print("Product not found!")
        elif choice == "3":
            update_stock(products)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

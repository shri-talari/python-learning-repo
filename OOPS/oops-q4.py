'''Q4. Online Shopping System (Abstraction + Collections + Exception Handling)

Problem:

Define an abstract class Product with abstract method get_price().

Derive classes:

Electronics, Clothing, Grocery → each returns its own price with possible discounts.

Create a Cart class that:

Adds products (store in list).

Displays unique items (set).

Stores cart summary in a file (cart.txt).

Handle invalid inputs and missing products.'''

from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    @abstractmethod
    def get_price(self):
        pass


class Electronics(Product):
    def get_price(self):
        discount = 0.15
        return self.base_price * (1 - discount)


class Clothing(Product):
    def get_price(self):
        discount = 0.2
        return self.base_price * (1 - discount)


class Groceries(Product):
    def get_price(self):
        discount = 0.1
        return self.base_price * (1 - discount)


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only Products can be added to the cart")
        self.products.append(product)

    def display_unique_items(self):
        unique_names = set(p.name for p in self.products)
        print("\nUnique items in cart:")
        for item in unique_names:
            print(item)

    def save_cart_summary(self):
        try:
            with open("cart.txt", "w") as f:
                for p in self.products:
                    f.write(f"{p.name} - {p.get_price():.2f}Rs\n")
            print("\nCart summary saved to 'cart.txt'")
        except Exception as e:
            print("Error writing to file:", e)


def create_product(category, name, price):
    if category == "Electronics":
        return Electronics(name, price)
    elif category == "Clothing":
        return Clothing(name, price)
    elif category == "Grocery":
        return Groceries(name, price)
    else:
        raise ValueError(f"Unknown product category: {category}")


def main():
    cart = Cart()

    while True:
        try:
            print("\n--- Add Product to Cart ---")
            category = input(
                "Enter category (Electronics/Clothing/Grocery or 'q' to quit): ")
            if category.lower() == 'q':
                break

            name = input("Enter product name: ")
            price_input = input("Enter product price: ")

            try:
                price = float(price_input)
                if price <= 0:
                    raise ValueError("Price must be positive.")
            except ValueError:
                print("Invalid price. Must be a positive number.")
                continue

            product = create_product(category, name, price)
            cart.add_product(product)
            print(f"{name} added to cart.")

        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
        except Exception as e:
            print("Unexpected error:", e)

    cart.display_unique_items()
    cart.save_cart_summary()


if __name__ == "__main__":
    main()

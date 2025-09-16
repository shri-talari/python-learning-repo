'''Q2. Library Management System (Inheritance + File Handling)**

Problem:

Create a base class Book with attributes: title, author, copies.

Create a derived class Library with:

Method to add_book(), borrow_book(), return_book().

Store book records in a file (library.txt).

Handle:

Borrowing unavailable books (ValueError).

Adding invalid copies (negative numbers).

Use dictionary internally {title: copies}.'''


class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies


class Library(Book):
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        books_dict = {}
        try:
            with open("library.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        title, author, copies = parts
                        books_dict[title] = {
                            "author": author,
                            "copies": int(copies)
                        }
        except FileNotFoundError:
            open("library.txt", "w").close()
        return books_dict

    def save_books(self):
        with open("library.txt", "w") as file:
            for title, info in self.books.items():
                file.write(f"{title},{info['author']},{info['copies']}\n")

    def add_book(self, title, author, copies):
        try:
            if copies < 0:
                raise ValueError("Cannot add negative number of copies.")
            if title in self.books:
                self.books[title]["copies"] += copies
            else:
                self.books[title] = {"author": author, "copies": copies}
            self.save_books()
            print(f"Added '{title}' with {copies} copies.")
        except ValueError as e:
            print(f"Error: {e}")

    def borrow_book(self, title):
        try:
            if title not in self.books:
                raise ValueError("Book not found in the library.")
            if self.books[title]["copies"] == 0:
                raise ValueError("No copies available to borrow.")
            self.books[title]["copies"] -= 1
            self.save_books()
            print(f"You have borrowed '{title}'.")
        except ValueError as e:
            print(f"Error: {e}")

    def return_book(self, title):
        if title in self.books:
            self.books[title]["copies"] += 1
            print(f"You have returned '{title}'.")
        else:
            author = input(f"Enter author name for new book '{title}': ")
            self.books[title] = {"author": author, "copies": 1}
            print(f"New book '{title}' added on return.")
        self.save_books()


if __name__ == "__main__":
    library = Library()

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            try:
                copies = int(input("Enter number of copies: "))
                library.add_book(title, author, copies)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "2":
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)

        elif choice == "3":
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == "4":
            print("Exiting Library System.")
            break

        else:
            print("Invalid choice. Please try again.")

'''Q1. Library Book Management System

Problem:
Create a program to manage a small library system.

Store available books in a dictionary with keys = book titles (string) and values = copies available (int).

Use functions to:

add_book(title, copies) → Adds a book or increases existing copies.

borrow_book(title) → Decreases copies if available, otherwise raises and handles a ValueError (“Book not available”).

return_book(title) → Increases copies.

Ensure input handling:

If user enters a number instead of a string for book title, handle TypeError.

If copies entered are not integers, handle exceptions.

Display borrowed books (list), unique borrowed books (set), and a summary at the end.'''


def add_book(title, copies):
    if title in library:
        library[title] += copies
        print(f"Successfully increased the copies of '{title}'.")
    else:
        library[title] = copies
        print(f"Successfully added the book '{title}'.")


def borrow_book(title):
    if title in library and library[title] > 0:
        library[title] -= 1
        borrowed.append(title)
        print(f"Successfully borrowed '{title}'.")
    elif title in library:
        raise ValueError(f"'{title}' is out of stock.")
    else:
        raise ValueError(f"'{title}' is not available in the library.")


def return_book(title):
    if title in borrowed:
        library[title] = library.get(title, 0) + 1
        borrowed.remove(title)
        print(f"Successfully returned the book '{title}'.")
    else:
        print(f"Error: '{title}' was not borrowed from the library.")


library = {}
borrowed = []

input_books = int(input("Enter the number of initial books: "))
for i in range(input_books):
    while True:
        try:
            name = input(f"Enter the title of book {i + 1}: ")
            if name.isdigit():
                raise TypeError("Book title cannot be a number")
            copies = int(input(f"Enter the number of copies of '{name}': "))
            add_book(name, copies)
            break
        except TypeError as e:
            print(e)
        except ValueError:
            print("The number of copies must be an integer")

while True:
    print("""What would you like to do?
    1. Borrow a Book
    2. Return a Book
    3. Exit
    """)
    choice = int(input("Enter your action number: "))

    if choice == 1:
        title = input("Enter the title of the book you want to borrow: ")
        try:
            borrow_book(title)
        except ValueError as e:
            print(e)
    elif choice == 2:
        title = input("Enter the title of the book you want to return: ")
        return_book(title)
    elif choice == 3:
        print("Exited from the library system.")
        print(f"Borrowed Books: {borrowed}")
        print(f"Unique Borrowed Books: {set(borrowed)}")
        print(f"Library Summary: {library}")
        break
    else:
        print("Please enter a valid number (1-3).")

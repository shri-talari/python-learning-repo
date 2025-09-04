'''Q1. Inventory Management System (Lists and Strings)

Create a Python program to manage an inventory of products. The program should:

Allow the user to add new products to the inventory.

Display the current inventory list.

Find and display the product with the longest name.

Remove a product by its name (if it exists).

Display the total number of products in the inventory.

Use string manipulation to ensure the product names are case-insensitive 
(e.g., "apple" and "Apple" should be treated as the same). 
Use a list to store the products and allow the user to interact with the inventory system.'''

inventory = []

while True:
    print("""What operation you want to perform in the inventory ?
1.Display the current inventory list
2.Add new products to the inventory
3.Display the product with longest name
4.Remove a product
5.Display Total number of products in the inventory 
6.Exit the Inventory Management System \n""")

    choice = int(input("Enter the operation number that you want to perform : "))
    print("")
    if choice in [1,2,3,4,5,6]:
        if choice == 1:
            if inventory:
                [print(x.title()) for x in inventory]
                print("")
            else:
                print("Inventory is empty ! \n")
        elif choice == 2:
            new_prods = input("Enter the products you want to add seperated by comma : ").split(",")
            new_prods = [x.strip().lower() for x in new_prods]
            inventory.extend(new_prods)
            print(f"New Products {new_prods} added successfully !")
        elif choice == 3:
            if not inventory:
                print("The inventory is empty")
            else:
                longest = inventory[0]
                for prod in inventory:
                    if len(prod) > len(longest):
                        longest = prod
            print(f"The Product with longest name is {longest}")
        elif choice == 4:
            if not inventory:
                print("The inventory is empty")
            else:
                del_prod = input("Enter the name of product to be removed from inventory : ").strip().lower()
                inventory.remove(del_prod)
                print("Product successfully removed from the inventory. \n")
        elif choice == 5:
            print(f"Total number of Products in the inventory : {len(inventory)}")
        else:
            print("Exited from the Inventory Management System.\n")
            break
    else:
        print("Enter a valid operation number between 1 to 6.\n")


'''Q2. Palindrome Word Filter

Ask the user for a sentence.

Convert it all to lowercase, split into words, and store them in a list.

Build a new list containing only palindrome words (like "level", "madam").

If a palindrome’s length is odd, store it as a float (its length).

If a palindrome’s length is even, store it as a string ("word-length").

Print the final list.'''

sentence = input("Enter a sentence: ")
sentence = sentence.lower()
words = sentence.split()

palindromes = []

for word in words:
    if word == word[::-1]:
        length = len(word)
        if length % 2 == 1:
            palindromes.append(float(length))
        else:
            palindromes.append(word + "-" + str(length))

print("Final Palindrome List:", palindromes)


'''Q3. List Compression Challenge

Ask the user for a string of comma-separated values (mix of numbers and words).

Convert them into a list.

For every number, cast it to int and keep only even numbers.

For every word, keep it only if its first letter is a vowel.

Build and print the final filtered list.'''

values = input("Enter comma-separated values (numbers and words): ")
items = values.split(",")
filtered_list = []

for item in items:
    item = item.strip()   
    if item.isdigit():
        num = int(item)  
        if num % 2 == 0:  
            filtered_list.append(num)
    else:
        if len(item) > 0:  
            first_char = item[0].lower()
            if first_char in "aeiou":
                filtered_list.append(item)
print("Final Filtered List:", filtered_list)

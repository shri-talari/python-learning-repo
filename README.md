# Functions and Exceptions – Modular Code & Error Handling

This section introduces **functions for modular programming** and **exception handling** for robust code execution.  
It builds upon all previous concepts (Basics, Control Structures, Data Types & Collections).

---

## Concepts Covered

- Functions: definition, parameters, return values  
- Scope (local vs global variables)  
- Lambda functions  
- Exception handling: `try`, `except`, `finally`  
- Raising custom exceptions  

---

## Cumulative Learning

Each problem requires knowledge from:  
- Basics  
- Control Structures  
- Data Types & Collections  
- + Functions & Exception Handling introduced here  

---

## Problems Questions Solved (5 per topic)

---

### 🛠️ Functions

**Q1. List Operations with Functions**

Problem:
Write a function list_operations(numbers) that:

Takes a list of integers as input.

Returns a tuple containing:

The largest number

The smallest number

The sum of all numbers

A new set containing only unique even numbers.




**Q2. Student Grade Calculator**

Problem:
Write a function calculate_grade(marks) that:

Takes a dictionary where keys are subject names and values are marks (0–100).

Calculates the average marks.

Returns the grade based on the following:

>=90 → "A"

>=75 → "B"

>=50 → "C"

<50 → "F"

Also, write a program to take input from the user, store it in a dictionary, and print the student’s grade.




**Q3. Bank Account Simulation**

Problem:
Write a program with functions to simulate a simple bank system:

deposit(balance, amount) → adds money and returns new balance

withdraw(balance, amount) → subtracts money if balance is enough, else prints "Insufficient funds".

account_summary(transactions) → takes a list of transactions (as dictionaries) and returns total deposits, total withdrawals, and final balance.




**Q4. Word Frequency Counter**

Problem:
Write a function word_frequency(sentence) that:

Takes a string sentence.

Returns a dictionary with each word as the key and its frequency as the value.

Ignore case (treat "Hello" and "hello" as the same).




**Q5. Unique Elements Across Collections**

Problem:
Write a function unique_elements(data1, data2) that:

Takes a tuple and a list as input.

Combines them into a single set of unique elements.

Returns both the set and its length.




---

### ⚠️ Exceptions

**Q1. Student Grade Calculator with Error Handling**

Problem:
Write a program that accepts marks of N students (out of 100) from the user and stores them in a dictionary with student names as keys and marks as values.

If the user enters marks outside 0–100, raise and handle a ValueError.

If the user enters a non-integer value, handle the exception and prompt again.

Finally, display:

Highest scorer (name + marks)

Lowest scorer (name + marks)

Average score




**Q2. Safe Division with Multiple Exceptions**

Problem:
Write a function safe_divide(a, b) that:

Divides two numbers a and b.

Handles the following exceptions:

ZeroDivisionError: print "Cannot divide by zero!"

ValueError: if the inputs cannot be converted to floats.

Any other exception: print "Unexpected error occurred!".

Use a loop to allow the user to keep entering numbers until they enter "exit".




**Q3. Unique Word Counter with Error Handling**

Problem:
Write a program that takes a sentence as input, splits it into words, and counts the frequency of each unique word using a dictionary.

Handle the case when the user inputs an empty string (ValueError).

Handle numbers inside the sentence by converting them to strings and still counting.

Ignore punctuation marks.




**Q4. Shopping Cart Manager**

Problem:
Create a shopping cart system using a dictionary {item: price} and a list for purchased items.

Ask the user to enter items and their price.

If the price entered is invalid (non-numeric), handle the exception and re-ask.

If the user tries to purchase an item not in the dictionary, handle KeyError.

Allow the user to checkout and display:

Items purchased (as a tuple)

Total amount

Unique items purchased (as a set)




**Q5. ATM Simulator**

Problem:
Simulate a simple ATM system.

The account starts with balance = 1000.

User can:

Deposit money

Withdraw money

Check balance

Exit

Handle exceptions:

Non-integer deposit/withdraw amount (ValueError).

Withdrawal amount greater than balance (Exception).



---

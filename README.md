# Object-Oriented Programming (OOPS) - Building Real-World Models

This section introduces **Object-Oriented Programming (OOPS)** which is used to design programs using real-world concepts such as objects, classes, inheritance, polymorphism, and more.  
It builds upon all previous concepts (Basics, Control Structures, Data Types & Collections, Functions, Exception Handling, and File Handling).

---

## Concepts Covered

- Classes and Objects
- Constructors and Destructors
- Inheritance (Single, Multiple, Multilevel, Hierarchical)
- Polymorphism (Overloading, Overriding, Duck Typing)
- Encapsulation & Abstraction
- Magic Methods & Operator Overloading

---

## Cumulative Learning

Each problem requires knowledge from:

- Basics
- Control Structures
- Data Types & Collections
- Functions & Exception Handling
- File Handling
- - Object-Oriented Programming (OOPS)

---

## Problems Questions Solved (5 per topic)

---

### OOPS

**Q1. Bank Account System (Encapsulation + Exception Handling)**

Problem:

Create a BankAccount class with:

Attributes: account_number, holder_name, balance (private).

Methods:

deposit(amount) → adds money (handle invalid inputs).

withdraw(amount) → subtracts money (raise exception if insufficient funds).

get_balance() → returns balance.

Create multiple accounts and allow transactions.

Store transaction history in a file.

---

**Q2. Library Management System (Inheritance + File Handling)**

Problem:

Create a base class Book with attributes: title, author, copies.

Create a derived class Library with:

Method to add_book(), borrow_book(), return_book().

Store book records in a file (library.txt).

Handle:

Borrowing unavailable books (ValueError).

Adding invalid copies (negative numbers).

Use dictionary internally {title: copies}.

---

**Q3. Employee Payroll System (Polymorphism + Functions + File Handling)**

Problem:

Create a base class Employee with attributes: name, id, salary.

Derive classes:

FullTimeEmployee → salary = fixed monthly.

PartTimeEmployee → salary = hours × rate.

Override a method calculate_salary().

Write payroll results to payroll.txt.

Display: highest salary, lowest salary, average salary.

---

**Q4. Online Shopping System (Abstraction + Collections + Exception Handling)**

Problem:

Define an abstract class Product with abstract method get_price().

Derive classes:

Electronics, Clothing, Grocery → each returns its own price with possible discounts.

Create a Cart class that:

Adds products (store in list).

Displays unique items (set).

Stores cart summary in a file (cart.txt).

Handle invalid inputs and missing products.

---

**Q5.University System (OOP Integration Challenge)**
Problem:

Create classes:

Person (base) → attributes: name, age.

Student(Person) → attributes: roll_no, marks (dict of subject: score).

Professor(Person) → attributes: employee_id, courses (tuple).

Functions:

For students → calculate average, highest subject.

For professors → display courses.

Store all records in a file (university.txt).

Handle exceptions: invalid marks, missing data, file errors.

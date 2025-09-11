# File Handling - Working with files to store data permanently

This section introduces **File Handling** which is used to work with different files and perform various operations on them to store data on device storage permanently.  
It builds upon all previous concepts (Basics, Control Structures, Data Types & Collections, Functions and Exception Handling).

---

## Concepts Covered

- File Handling 
- File Modes
- Open, Read, Write Files
- Working with Binary Files
---

## Cumulative Learning

Each problem requires knowledge from:  
- Basics  
- Control Structures  
- Data Types & Collections  
- Functions & Exception Handling 
- + File Handling

---

## Problems Questions Solved (5 per topic)

---

### File Handling

**Q1. Student Record Manager (CSV File Simulation)**

Problem:
Create a program that manages student records stored in a text file.

Each record = "name,marks" (one per line).

Write a function to:

Add a new student record.

Read all records and display highest, lowest, and average marks.

Handle exceptions:

File not found.

Invalid marks (non-numeric or <0 or >100).

Ensure duplicate names are handled by overwriting the existing record.




**Q2. Word Frequency Counter (File Version)**

Problem:
Write a program that:

Reads a text file.

Cleans punctuation and splits into words.

Stores word frequencies in a dictionary.

Displays:

Top 5 most frequent words.

Unique word count.

Handle exceptions:

File not found.

Empty file.




**Q3. Employee Payroll System (File-Based)**

Problem:
Extend payroll to file handling:

Input employee details: name, hours_worked, hourly_rate.

Calculate salary and store results in payroll.txt.

At the end, read the file and display:

Employee with max salary.

Employee with min salary.

Average salary.

Handle exceptions:

Negative hours/rate.

Non-numeric values.

File read/write errors.




**Q4. Shopping Cart with File Persistence**

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

File missing.




**Q5.Quiz Game with File Storage**

Problem:
Create a quiz game using file handling.

Questions are stored in a file (questions.txt) in format:
"question|option1,option2,option3|answer"

Program reads questions and asks user.

User’s answers are stored in answers.txt.

At the end, show:

Score.

Correctly answered questions (set).

Summary dictionary {question: chosen_answer}.

Handle exceptions:

Invalid file format.

File not found.

Invalid user input.




---

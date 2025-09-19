# Python Modules & Libraries - Powering Real-World Applications

This section introduces **Python’s Standard Library modules** which provide built-in functionality to interact with the operating system, handle data formats, manage time, and more.  
It builds upon all previous concepts (Basics, Control Structures, Data Types & Collections, Functions, Exception Handling, File Handling, and OOPS).

---

## Concepts Covered

- Using and Importing Modules  
- Commonly Used Python Standard Libraries:  
  - `os`  
  - `shutil`  
  - `datetime`  
  - `json`    

---

## Cumulative Learning

Each problem requires knowledge from:  
- Basics  
- Control Structures  
- Data Types & Collections  
- Functions & Exception Handling  
- File Handling  
- Object-Oriented Programming (OOPS)  
- + Modules & Libraries  

---

## Problems Questions Solved (2–4 per module)

---

### OS and Shutil Module
  
**Q1. File Organizer**  
Problem: Write a script to organize files in a folder into subfolders based on file extension.  
Example: all .txt files go into TextFiles, all .jpg files into Images.

Handle errors:

Non-existing directory (FileNotFoundError).

Permission errors.

Ensure it doesn’t move system/hidden files accidentally.


**Q2.Backup and Restore Utility (OOP + os + shutil)**

Problem:
Design a backup tool:

Class BackupManager:

backup(source_dir, backup_dir) → copies all files.

restore(backup_dir, restore_dir) → restores files.

Use os.walk() to handle nested folders.

Add error handling for:

Missing source directory.

Permission issues.

Maintain a log file of operations.

**Q3. Log File Analyzer (File Handling + os + Exception Handling)**

Problem:

Given a folder containing multiple log files (.log), write a program to:

Read all .log files.

Count occurrences of “ERROR”, “WARNING”, and “INFO”.

Write a summary report into summary.txt.

Handle: missing log files, empty files, and encoding errors.


---

### Regular Expression (re) Module

**Q1. Log File Analyzer (Find Errors)**

Suppose you are given a server log file server.log containing lines like:
Write a program that:

Reads the log file.

Uses regex to extract all ERROR messages.

Prints them along with the timestamps.


**Q2. Password Strength Checker**

Write a program that asks the user to enter a password and checks if it is strong using regex rules:

Minimum 8 characters

At least one uppercase letter

At least one lowercase letter

At least one digit

At least one special character (@, #, $, %, &, *)

If password fails, raise an exception and show which rule(s) are violated.



**Q3. Data Extraction – Invoice Parser**

You are given a string containing multiple invoices in this format:
Write a Python program using regex that extracts:

Invoice number

Date

Amount

Store the extracted data into a dictionary list and print it.

### JSON Module

**Q1. Student Marks Database** 

Write a program that: 
Maintains a students.json file containing student data in this format: 
[ {"name": "Rahul", "marks": 85}, {"name": "Neha", "marks": 92} ] 
Allows the user to: Add a new student with marks. View all students. 
Ensure data is updated and saved back in the JSON file.'
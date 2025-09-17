# Python Modules & Libraries - Powering Real-World Applications

This section introduces **Python’s Standard Library modules** which provide built-in functionality to interact with the operating system, handle data formats, manage time, and more.  
It builds upon all previous concepts (Basics, Control Structures, Data Types & Collections, Functions, Exception Handling, File Handling, and OOPS).

---

## Concepts Covered

- Using and Importing Modules  
- Commonly Used Python Standard Libraries:  
  - `os`  
  - `sys`  
  - `datetime`  
  - `json`  
  - `pickle`  
  - (others can be added as explored)  

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

### OS Module
  
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


---



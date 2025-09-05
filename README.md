
---

## 🧺 `data-types-and-collections/README.md`

```markdown
# 🧺 Data Types and Collections – Strings, Lists, Sets, Tuples, Dicts

This section explores Python’s powerful **built-in data structures**. Each group of problems builds on earlier concepts and introduces more efficient data handling.

---

## 📘 Concepts Covered

- String methods & slicing
- Lists: indexing, appending, list comprehension
- Tuples: immutability
- Sets: uniqueness, set operations
- Dictionaries: key-value pairs, iteration

---

## 🔄 Cumulative Learning

Each problem requires knowledge from:
- Basics
- Control Structures
- + Data Structures introduced here

---

## 📂 Problems Questions Solved (3 per data type)

### 🔤 Strings

### Q1. Enhanced Calculator with String Formatting

**Problem:**
Write a Python program that asks the user for two numbers (as strings) and performs the following operations: addition, subtraction, multiplication, and division. Each result should be displayed in a formatted string, indicating which operation was performed. Ensure that the numbers are correctly cast to the appropriate numeric data types before performing the operations. Handle division by zero gracefully.

Additionally, use string formatting to present the results

### Q2. Sentence Analysis - Word Count and Length

**Problem:**
Create a Python program that asks the user for a sentence (string) and:

Counts the number of words in the sentence.

Finds the length of the longest word.

Finds the shortest word.

You should handle edge cases such as multiple spaces between words

### Q3. String Conversion and Comparison

**Problem:**
Write a Python program that:

Accepts two string inputs.

Converts both strings to lowercase and compares whether they are identical (ignoring case).

If they are not identical, the program should return the difference between the two strings (i.e., what characters are different and where).

Use string methods like lower(), strip(), and comparison operators to handle the task.'''

### 📋 Lists

### Q1. Inventory Management System (Lists and Strings)

**Problem:**
Create a Python program to manage an inventory of products. The program should:

Allow the user to add new products to the inventory.

Display the current inventory list.

Find and display the product with the longest name.

Remove a product by its name (if it exists).

Display the total number of products in the inventory.

Use string manipulation to ensure the product names are case-insensitive 
(e.g., "apple" and "Apple" should be treated as the same). 
Use a list to store the products and allow the user to interact with the inventory system.

### Q2. Palindrome Word Filter


**Problem:**
Ask the user for a sentence.

Convert it all to lowercase, split into words, and store them in a list.

Build a new list containing only palindrome words (like "level", "madam").

If a palindrome’s length is odd, store it as a float (its length).

If a palindrome’s length is even, store it as a string ("word-length").

Print the final list.


### List Compression Challenge

**Problem:**
Ask the user for a string of comma-separated values (mix of numbers and words).

Convert them into a list.

For every number, cast it to int and keep only even numbers.

For every word, keep it only if its first letter is a vowel.

Build and print the final filtered list.


### 🎯 Tuples

### Q1. Student Records Manager 

**Problem:**
Input: Names and marks of 5 students (marks entered as comma-separated string, cast to integers).

Store each student’s data as a tuple (name, [marks]) in a list.

Task:

Compute each student’s total & average marks.

Print: "Name | Total | Average | Pass/Fail" (Pass if avg ≥ 40).

Identify the topper (highest average).


### Q2. Movie Ratings Tracker

**Problem:**
You have a tuple of movies:
("Inception", "Interstellar", "Memento", "Tenet")

User enters ratings (1–10) for each movie as space-separated input (cast to integers).

Task:

Store movie and rating pairs as tuples inside a list.

Print all movies with ratings.

Identify the highest & lowest rated movies.

Print only movies with rating ≥ 8.

### Q3. Tuple-based Data Cleaner

**Problem:**
Input: Tuple of mixed values: ("45", 23, "0", 0, "18", 9, "hello", "7")

Task:

Extract only numeric values (cast them all to integers).

Store them in a list and remove zeros.

Print:

Cleaned list

Sum and average of values

Maximum and minimum


### 🔘 Sets



### 🔑 Dictionaries



---


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

---

### 🔤 Strings

- **Q1. Enhanced Calculator with String Formatting**  
  Write a Python program that asks the user for two numbers (as strings) and performs the following operations: addition, subtraction, multiplication, and division. Each result should be displayed in a formatted string, indicating which operation was performed. Ensure that the numbers are correctly cast to the appropriate numeric data types before performing the operations. Handle division by zero gracefully. Additionally, use string formatting to present the results.  

- **Q2. Sentence Analysis – Word Count and Length**  
  Create a Python program that asks the user for a sentence (string) and:  
  - Counts the number of words in the sentence.  
  - Finds the length of the longest word.  
  - Finds the shortest word.  
  Handle edge cases such as multiple spaces between words.  

- **Q3. String Conversion and Comparison**  
  Write a Python program that:  
  - Accepts two string inputs.  
  - Converts both strings to lowercase and compares whether they are identical (ignoring case).  
  - If they are not identical, return the difference between the two strings (i.e., what characters are different and where).  
  Use string methods like `lower()`, `strip()`, and comparison operators.  

---

### 📋 Lists

- **Q1. Inventory Management System (Lists and Strings)**  
  Create a Python program to manage an inventory of products. The program should:  
  - Allow the user to add new products to the inventory.  
  - Display the current inventory list.  
  - Find and display the product with the longest name.  
  - Remove a product by its name (if it exists).  
  - Display the total number of products.  
  Ensure product names are case-insensitive.  

- **Q2. Palindrome Word Filter**  
  - Ask the user for a sentence.  
  - Convert it to lowercase, split into words, and store them in a list.  
  - Build a new list containing only palindrome words.  
  - If a palindrome’s length is odd, store it as a float (its length).  
  - If a palindrome’s length is even, store it as a string (`"word-length"`).  
  - Print the final list.  

- **Q3. List Compression Challenge**  
  - Ask the user for a string of comma-separated values (mix of numbers and words).  
  - Convert them into a list.  
  - For every number, cast it to `int` and keep only even numbers.  
  - For every word, keep it only if its first letter is a vowel.  
  - Build and print the final filtered list.  

---

### 🎯 Tuples

- **Q1. Student Records Manager**  
  Input: Names and marks of 5 students (marks entered as comma-separated string, cast to integers).  
  Store each student’s data as a tuple `(name, [marks])` in a list.  
  Tasks:  
  - Compute each student’s total & average marks.  
  - Print: `"Name | Total | Average | Pass/Fail"` (Pass if avg ≥ 40).  
  - Identify the topper (highest average).  

- **Q2. Movie Ratings Tracker**  
  You have a tuple of movies: `("Inception", "Interstellar", "Memento", "Tenet")`  
  User enters ratings (1–10) for each movie as space-separated input.  
  Tasks:  
  - Store movie and rating pairs as tuples inside a list.  
  - Print all movies with ratings.  
  - Identify the highest & lowest rated movies.  
  - Print only movies with rating ≥ 8.  

- **Q3. Tuple-based Data Cleaner**  
  Input: Tuple of mixed values: `("45", 23, "0", 0, "18", 9, "hello", "7")`  
  Tasks:  
  - Extract only numeric values (cast them all to integers).  
  - Store them in a list and remove zeros.  
  - Print:  
    - Cleaned list  
    - Sum and average of values  
    - Maximum and minimum  

---

### 🔘 Sets

- **Q1. Unique Word Extractor**  
  Input: A sentence string.  
  Tasks:  
  - Convert to lowercase, split into words.  
  - Store all unique words in a set.  
  - Print count of unique words and the set itself (unordered).  

- **Q2. Word Comparison Between Two Sentences**  
  Input: Two sentences.  
  Tasks:  
  - Create sets of words for each.  
  - Print:  
    - Common words (intersection)  
    - Words only in first sentence  
    - Words only in second sentence  
    - Total unique words across both  

- **Q3. Duplicate Remover from Mixed Data**  
  Input: A tuple with duplicates: `("10", 20, "20", 30, "10", 40, 20, "30")`  
  Tasks:  
  - Convert all items to integers.  
  - Store unique values in a set.  
  - Convert back to a sorted list and print it.  

---

### 🔑 Dictionaries

- **Q1. Student Gradebook System**  
  Input:  
  - Student names and their marks in 3 subjects (example: `"Alice: 78, 85, 90"`)  
  - Store data in a nested dictionary `{student: {subject: mark}}`.  
  Tasks:  
  1. Compute total and average marks for each student.  
  2. Print `"Pass"` if average ≥ 40 else `"Fail"`.  
  3. Identify the overall topper (highest average).  
  4. Identify the topper for each subject.  


**Q2: Inventory and Billing System**

Input:
- Two dictionaries:
  inventory = {"apple": 10, "banana": 5, "milk": 2, "bread": 4}
  prices = {"apple": 30, "banana": 10, "milk": 50, "bread": 40}
- A purchase list entered by the user as comma-separated items (example: "apple, banana, milk, milk, bread").

Tasks:
1. For each item in the purchase list:
   - If item exists in inventory and stock > 0, reduce stock by 1 and add its price to the total bill.
   - If stock = 0, print "Out of stock".
   - If "milk" is bought more than 3 times, stop billing further (use break).
2. At the end, print the total bill and the updated inventory dictionary.

**Q3: Word Frequency Analyzer**

Input:
- A paragraph string entered by the user.

Tasks:
1. Convert the string to lowercase and split it into words.
2. Count the frequency of each word using a dictionary.
3. Print the dictionary sorted by frequency (highest first).
4. Identify and print the most frequent word(s).
5. Print the number of unique words using a set.


---

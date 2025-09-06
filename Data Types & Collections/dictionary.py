"""
Q1: Student Gradebook System

Input:
- Student names and their marks in 3 subjects (example: "Alice: 78, 85, 90").
- Store each student’s data in a nested dictionary where the key is the student’s name and value is another dictionary of subject:mark pairs.

Tasks:
1. Compute the total and average marks for each student.
2. Print "Pass" if average >= 40 else "Fail".
3. Identify and print the overall topper (highest average).
4. Identify and print the topper for each subject.
"""

students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    entry = input(f"Enter data for student {i+1} (format: Name: m1, m2, m3): ")
    name, marks_str = entry.split(":")
    marks = [int(x) for x in marks_str.split(",")]
    students[name.strip()] = {
        "Subject1": marks[0],
        "Subject2": marks[1],
        "Subject3": marks[2]
    }

print("\nName | Total | Average | Result")
overall_topper = ""
highest_avg = -1

subject_topper = {"Subject1": ("", -1), "Subject2": ("", -1), "Subject3": ("", -1)}

for name, marks_dict in students.items():
    total = 0
    count = 0
    for subject, mark in marks_dict.items():
        total += mark
        count += 1
        if mark > subject_topper[subject][1]:
            subject_topper[subject] = (name, mark)
    avg = total / count
    result = "Pass" if avg >= 40 else "Fail"
    print(name, "|", total, "|", round(avg,2), "|", result)
    if avg > highest_avg:
        highest_avg = avg
        overall_topper = name
print(f"\nOverall Topper: {overall_topper} with average {highest_avg:.2f}")

print("\nSubject Toppers:")
for subject, (name, mark) in subject_topper.items():
    print(subject, ":", name, "with", mark)


"""
Q2: Inventory and Billing System

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
"""

inventory = {"apple": 10, "banana": 5, "milk": 2, "bread": 4}
prices = {"apple": 30, "banana": 10, "milk": 50, "bread": 40}

purchase_input = input("Enter items to purchase (comma separated): ")
purchase_list = [item.strip().lower() for item in purchase_input.split(",")]

total_bill = 0
milk_count = 0

for item in purchase_list:
    if item in inventory:   
        if inventory[item] > 0:
            inventory[item] -= 1
            total_bill += prices[item]

            if item == "milk":
                milk_count += 1
                if milk_count > 3:
                    print("Milk bought more than 3 times. Stopping billing further.")
                    break
        else:
            print(item, "is Out of stock")
    else:
        print(item, "not found in inventory")
print("\nTotal Bill:", total_bill)
print("Updated Inventory:", inventory)


"""
Q3: Word Frequency Analyzer

Input:
- A paragraph string entered by the user.

Tasks:
1. Convert the string to lowercase and split it into words.
2. Count the frequency of each word using a dictionary.
3. Print the dictionary sorted by frequency (highest first).
4. Identify and print the most frequent word(s).
5. Print the number of unique words using a set.
"""

paragraph = input("Enter a paragraph: ").lower()

words = paragraph.split()

freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

max_count = max(sorted_freq.values())
most_frequent = [word for word, count in sorted_freq.items() if count == max_count]

unique_words = set(words)

print("\nWord Frequencies (sorted):", sorted_freq)
print("Most frequent word(s):", most_frequent, "with count:", max_count)
print("Number of unique words:", len(unique_words))

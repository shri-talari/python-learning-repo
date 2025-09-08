'''Q2. Student Grade Calculator

Problem:
Write a function calculate_grade(marks) that:

Takes a dictionary where keys are subject names and values are marks (0–100).

Calculates the average marks.

Returns the grade based on the following:

>=90 → "A"

>=75 → "B"

>=50 → "C"

<50 → "F"

Also, write a program to take input from the user, store it in a dictionary, and print the student’s grade.'''


def calculate_grade(marks):
    total = 0
    average = 0
    values = marks.values()
    for mark in values:
        total += mark
    average = total/len(marks)
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"
    return average, grade


subject_marks = {}
subjects = int(input("Enter the number of subjects: "))

for i in range(subjects):
    subject = input(f"Enter name of subject {i+1}: ")
    score = int(input(f"Enter marks for {subject}: "))

    if score < 0 or score > 100:
        print("Please enter only valid marks between 0 and 100.")
        exit()

    subject_marks[subject] = score

avg, result = calculate_grade(subject_marks)
print(f" Average = {avg:.2f}\n Grade = {result}")

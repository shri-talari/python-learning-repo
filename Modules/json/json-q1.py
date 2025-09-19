'''Q1. Student Marks Database 

Write a program that: 
Maintains a students.json file containing student data in this format: 
[ {"name": "Rahul", "marks": 85}, {"name": "Neha", "marks": 92} ] 
Allows the user to: Add a new student with marks. View all students. 
Ensure data is updated and saved back in the JSON file.'''

import json
import os

FILE_NAME = "students.json"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        json.dump([], file)


def load_students():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    name = input("Enter the student's name: ")
    marks = input("Enter the student's marks: ")
    try:
        marks = int(marks)
        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number for marks.")
        return

    student = {"name": name, "marks": marks}
    students = load_students()
    students.append(student)
    save_students(students)
    print(f"Student {name} added successfully.")


def view_students():
    students = load_students()
    if not students:
        print("No students found.")
        return

    print("\nStudent List:")
    for student in students:
        print(f"Name: {student['name']}, Marks: {student['marks']}")


def main():
    while True:
        print("\n1. Add a new student")
        print("2. View all students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

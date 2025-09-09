'''Q1. Student Grade Calculator with Error Handling

Problem:
Write a program that accepts marks of N students (out of 100) from the user and stores them in a dictionary 
with student names as keys and marks as values.

If the user enters marks outside 0–100, raise and handle a ValueError.

If the user enters a non-integer value, handle the exception and prompt again.

Finally, display:

Highest scorer (name + marks)

Lowest scorer (name + marks)

Average score'''


students = {}

no_of_students = int(input("Enter the number of students : "))
for i in range(no_of_students):
    name = input(f"Enter the name of student {i+1}: ").strip()
    while True:
        try:
            marks = int(input(f"Enter the marks of {name}: "))
            if marks < 0 or marks > 100:
                raise ValueError
            else:
                students[name] = marks
                break
        except ValueError:
            print("Invalid Marks ! Please enter marks in range 0-100")

if students:
    highest = max(students, key=students.get)
    lowest = min(students, key=students.get)
    average = sum(students.values()) / len(students)

    print(f"Highest Scorer : {highest} with {students[highest]} marks")
    print(f"Lowest Scorer : {lowest} with {students[lowest]} marks")
    print(f"Average score : {average:.2f}")
else:
    print("No student data entered.")

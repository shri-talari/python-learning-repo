'''Q1. Student Record Manager (CSV File Simulation)

Problem:
Create a program that manages student records stored in a text file.

Each record = "name,marks" (one per line).

Write a function to:

Add a new student record.

Read all records and display highest, lowest, and average marks.

Handle exceptions:

File not found.

Invalid marks (non-numeric or <0 or >100).

Ensure duplicate names are handled by overwriting the existing record.'''


def read_records():
    records = {}
    try:
        with open("Files\\file1.txt", "r") as f:
            for line in f:
                if line.strip():
                    parts = line.strip().split(",")
                    if len(parts) == 2:
                        name = parts[0]
                        try:
                            marks = int(parts[1])
                            records[name] = marks
                        except ValueError:
                            continue
    except FileNotFoundError:
        pass
    return records


def write_records(records):
    try:
        with open("Files\\file1.txt", "w") as f:
            for name in records:
                f.write(name + "," + str(records[name]) + "\n")
    except:
        print("Error writing to file.")


def add_student(name, marks):
    try:
        marks = int(marks)
        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Error: Marks must be a valid number.")
        return

    records = read_records()
    records[name] = marks
    write_records(records)
    print("Record added/updated successfully.")


def display_all_records():
    records = read_records()
    if not records:
        print("No records found.")
        return

    print("\nAll Student Records:")
    for name in records:
        print(name + ": " + str(records[name]))


def analyze_records():
    records = read_records()
    if not records:
        print("No records to analyze.")
        return

    marks_list = list(records.values())

    highest = max(marks_list)
    lowest = min(marks_list)
    total = sum(marks_list)
    average = total / len(marks_list)

    highest_students = []
    lowest_students = []

    for name in records:
        if records[name] == highest:
            highest_students.append(name)
        if records[name] == lowest:
            lowest_students.append(name)

    print("\n--- Record Analysis ---")
    print(f"{highest_students} got highest marks : {highest}")
    print(f"{lowest_students} got lowest marks : {lowest}")
    print("Average Marks:", round(average, 2))


while True:
    print("\n--- Student Record Manager ---")
    print("1. Add Student Record")
    print("2. Display All Records")
    print("3. Analyze Records")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = input("Enter student marks: ")
        add_student(name, marks)

    elif choice == "2":
        display_all_records()

    elif choice == "3":
        analyze_records()

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1-4.")

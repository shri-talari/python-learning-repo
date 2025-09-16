'''Q5.University System (OOP Integration Challenge)**
Problem:

Create classes:

Person (base) → attributes: name, age.

Student(Person) → attributes: roll_no, marks (dict of subject: score).

Professor(Person) → attributes: employee_id, courses (tuple).

Functions:

For students → calculate average, highest subject.

For professors → display courses.

Store all records in a file (university.txt).

Handle exceptions: invalid marks, missing data, file errors.'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks

    def calculate_average(self):
        try:
            if not self.marks:
                raise ValueError("Marks data is missing.")
            total_marks = sum(self.marks.values())
            num_subjects = len(self.marks)
            return total_marks / num_subjects
        except Exception as e:
            print(f"Error calculating average: {e}")
            return None

    def highest_subject(self):
        try:
            if not self.marks:
                raise ValueError("Marks data is missing.")
            highest_subject = max(self.marks, key=self.marks.get)
            highest_score = self.marks[highest_subject]
            return highest_subject, highest_score
        except Exception as e:
            print(f"Error finding highest subject: {e}")
            return None


class Professor(Person):
    def __init__(self, name, age, employee_id, courses):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.courses = courses

    def display_courses(self):
        try:
            if not self.courses:
                raise ValueError("Courses data is missing.")
            return ', '.join(self.courses)
        except Exception as e:
            print(f"Error displaying courses: {e}")
            return None


def store_records(students, professors, filename="university.txt"):
    try:
        with open(filename, 'w') as file:
            file.write("University Records\n")
            file.write("=================================\n\n")

            file.write("Students:\n")
            for student in students:
                file.write(
                    f"Name: {student.name}, Age: {student.age}, Roll No: {student.roll_no}\n")
                file.write(f"Marks: {student.marks}\n")
                avg = student.calculate_average()
                if avg is not None:
                    file.write(f"Average Marks: {avg:.2f}\n")
                highest_subject, highest_score = student.highest_subject()
                if highest_subject:
                    file.write(
                        f"Highest Scoring Subject: {highest_subject} with score: {highest_score}\n")
                file.write("\n")

            file.write("Professors:\n")
            for professor in professors:
                file.write(
                    f"Name: {professor.name}, Age: {professor.age}, Employee ID: {professor.employee_id}\n")
                courses = professor.display_courses()
                if courses:
                    file.write(f"Courses Taught: {courses}\n")
                file.write("\n")

            print(f"Records have been stored in {filename}.")

    except Exception as e:
        print(f"Error saving records to file: {e}")


def main():
    student1 = Student("Alice", 20, "S101", {
                       "Math": 90, "Science": 80, "History": 85})
    student2 = Student("Bob", 21, "S102", {
                       "Math": 70, "Science": 65, "History": 80})
    professor1 = Professor("Dr. Smith", 45, "P1001",
                           ("Math 101", "Physics 202"))
    professor2 = Professor("Dr. Johnson", 50, "P1002",
                           ("Computer Science 301", "Chemistry 302"))

    students = [student1, student2]
    professors = [professor1, professor2]

    store_records(students, professors)


if __name__ == "__main__":
    main()

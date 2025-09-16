'''Q3. Employee Payroll System (Polymorphism + Functions + File Handling)**

Problem:

Create a base class Employee with attributes: name, id, salary.

Derive classes:

FullTimeEmployee → salary = fixed monthly.

PartTimeEmployee → salary = hours × rate.

Override a method calculate_salary().

Write payroll results to payroll.txt.

Display: highest salary, lowest salary, average salary.'''


class Employee:
    def __init__(self, name, emp_id, salary=0):
        self.name = name
        self.id = emp_id
        self.salary = salary

    def calculate_salary(self):
        pass

    @staticmethod
    def analyze():
        try:
            with open("payroll.txt", "r") as f:
                employees = []
                total_salary = 0
                for line in f:
                    name, emp_id, salary = line.strip().split(",")
                    salary = float(salary)
                    employees.append((name, emp_id, salary))
                    total_salary += salary

                if not employees:
                    print("No payroll data available.")
                    return

                employees.sort(key=lambda x: x[2])

                highest = employees[-1]
                lowest = employees[0]
                average = total_salary / len(employees)

                print(
                    f"Highest Salary Employee: {highest[0]} (ID: {highest[1]}) → ${highest[2]}")
                print(
                    f"Lowest Salary Employee: {lowest[0]} (ID: {lowest[1]}) → ${lowest[2]}")
                print(f"Average Salary: ${average:.2f}")

        except FileNotFoundError:
            print("Payroll file not found.")
        except Exception:
            print("Something went wrong. Please try again later.")


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        try:
            with open("payroll.txt", "a") as f:
                f.write(f"{self.name},{self.id},{self.salary}\n")
        except Exception:
            print("Error writing full-time employee salary.")


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours, rate):
        super().__init__(name, emp_id)
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        self.salary = self.hours * self.rate
        try:
            with open("payroll.txt", "a") as f:
                f.write(f"{self.name},{self.id},{self.salary}\n")
        except Exception:
            print("Error writing part-time employee salary.")


with open("payroll.txt", "w") as f:
    pass

emp1 = FullTimeEmployee("Alice", 1, 3000)
emp2 = PartTimeEmployee("Bob", 2, 30, 15)
emp3 = PartTimeEmployee("Charlie", 3, 40, 25)
emp4 = FullTimeEmployee("Darwin", 4, 2500)

for emp in [emp1, emp2, emp3, emp4]:
    emp.calculate_salary()

Employee.analyze()

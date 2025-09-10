'''Q2. Employee Payroll System with Error Handling

Problem:
Build a payroll system that:

Takes input for N employees.

Each employee is stored in a dictionary with fields: name, hours_worked, hourly_rate, salary.

Calculate salary = hours_worked * hourly_rate.

Apply conditions:

If hours_worked < 0 or hourly_rate < 0, raise and handle a ValueError.

If non-numeric values entered for hours/rate, handle ValueError.

Use a loop to calculate payroll for all employees.

At the end, display:

Employee with maximum salary.

Employee with minimum salary.

Average salary.'''


employees = []
no_of_employees = int(input("Enter the number of employees: "))
for i in range(no_of_employees):
    employee = {}
    name = input(f"Enter name of employee {i+1}: ")
    while True:
        try:
            hours_worked = int(input(f"Enter hours worked for {name}:"))
            hourly_rate = int(input(f"Enter hourly rate for {name}:"))
            if hours_worked >= 0 and hourly_rate >= 0:
                employee["name"] = name
                employee["hours worked"] = hours_worked
                employee["hourly rate"] = hourly_rate
                employee["salary"] = hours_worked * hourly_rate
                employees.append(employee)
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input hours cannot be negative ! enter again")
        except TypeError:
            print("Invalid input hours should only be integer numbers ! enter again")

min_salary = employees[0]["salary"]
max_salary = employees[0]["salary"]
max_name = employees[0]["name"]
min_name = employees[0]["name"]
total = 0

for emp in employees:
    if emp["salary"] > max_salary:
        max_salary = emp["salary"]
        max_name = emp["name"]
    if emp["salary"] < min_salary:
        min_salary = emp["salary"]
        min_name = emp["name"]
    total += emp["salary"]

print(f"Employee with Maximum Salary : {max_name} - ${(max_salary)} ")
print(f"Employee with Minimum Salary : {min_name} - ${(min_salary)} ")
print(f"Average Salary : ${total/len(employees)} ")

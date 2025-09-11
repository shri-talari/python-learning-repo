'''Q3. Employee Payroll System (File-Based)

Problem:
Extend payroll to file handling:

Input employee details: name, hours_worked, hourly_rate.

Calculate salary and store results in payroll.txt.

At the end, read the file and display:

Employee with max salary.

Employee with min salary.

Average salary.

Handle exceptions:

Negative hours/rate.

Non-numeric values.

File read/write errors.'''

no_of_emp = int(input("Enter the number of employees: "))
if no_of_emp > 0:
    for i in range(no_of_emp):
        name = input(f"Enter name of employee {i+1}: ")
        while True:
            try:
                hours_worked = int(input(f"Enter Hours worked for {name}: "))
                hourly_rate = int(input(f"Enter Hourly rate for {name}: "))
                if hours_worked > 0 and hourly_rate > 0:
                    try:
                        with open("Files\\payroll.txt", "a") as f:
                            f.write(name+","+str(hours_worked)+"," +
                                    str(hourly_rate)+","+str(hours_worked*hourly_rate)+"\n")
                            break
                    except FileNotFoundError:
                        print("File not found")
                else:
                    raise ValueError
            except ValueError:
                print("Hours can only be positive integers ! Please enter again")
employees = []

try:
    with open("Files\\payroll.txt", "r") as f:
        for line in f:
            name, hours_worked, hourly_rate, salary = line.strip().split(",")
            employees.append({
                "name": name,
                "hours": int(hours_worked),
                "rate": int(hourly_rate),
                "salary": int(salary)
            })
        if not employees:
            print("No data to process.")
        employees.sort(key=lambda x: x["salary"])
        max_emp = employees[-1]
        min_emp = employees[0]
        avg_salary = sum(emp['salary'] for emp in employees) / len(employees)

        print(
            f"\nEmployee with maximum salary: {max_emp['name']} - ${max_emp['salary']}")
        print(
            f"Employee with minimum salary: {min_emp['name']} - ${min_emp['salary']}")
        print(f"Average salary: ${avg_salary:.2f}")

except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print("An error occurred:", e)

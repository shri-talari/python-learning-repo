''' This file contains questions based on concepts of comments, variables, data types, casting and operators '''

''' Q1. Write a program that asks for the user's weight (in kilograms) and height (in meters). Then calculate their BMI (Body Mass Index).
Formula: BMI = weight / (height ** 2), Print the result rounded to two decimal places.'''

weight = float(input("Enter your weight in Kg : "))
height = float(input("Enter your height in Meters : "))

BMI = weight / (height ** 2)

print(f"Your BMI is {BMI:.2f}")

''' Q2. Write a program that converts the user's age from years into months, days, and hours.

Formulae:

months = years * 12

days = years * 365

hours = days * 24 '''

age = int(input("Enter your age in years : "))

days = age * 365
hours = days * 24

print(f"Your Age in months is {age * 12}")
print(f"Your Age in days is {days}")
print(f"Your Age in hours is {hours}")

''' Q3. Write a program that asks for a number (decimal or whole) from the user.

If it's a decimal, round it to the nearest integer. Then check if the rounded value is odd or even and print a corresponding message.'''

num = float(input("Enter a number : "))

if round(num) % 2 == 0:
    print(f"The number {num} rounded off to closest integer is even")
else:
    print(f"The number {num} rounded off to closest integer is odd")

''' Q4. Write a program that converts a string representing a number into both an integer and a float, and then prints both versions.

Example: If the input is "7.5", it should print 7 (integer) and 7.5 (float). '''

string = "10.5"
integer = int(float(string))

print(f"This is Integer version {integer}")
print(f"This is float version {float(string)}")
'''Q1. Grade Calculation with Conditions

Problem:
Write a Python program that takes a student's score as input (integer), checks the score, and prints the corresponding grade based on the following scale:

A: score >= 90

B: 70 <= score < 90

C: 50 <= score < 70

F: score < 50

If the input is not a valid integer, prompt the user again until a valid score is provided. '''

while True:
    score_input = input("Enter your exam score: ")

    if score_input.isdigit():
        score = int(score_input)
        if 0 <= score <= 100:
            if score >= 90:
                print("Your Grade is A")
            elif 70 <= score < 90:
                print("Your Grade is B")
            elif 50 <= score < 70:
                print("Your Grade is C")
            else:
                print("Your Grade is F")
            break
        else:
            print("Please enter a valid score between 0 to 100.")
    else:
        print("Invalid input! Please enter a valid integer score.")

''' Q2. Time Conversion

Problem:
Create a program that converts a given time in seconds into hours, minutes, and seconds. 
The input should be an integer representing the number of seconds. 
Ensure that the program handles various sizes of input (e.g., converting 3600 seconds to 1 hour, 0 minutes, and 0 seconds). 
Use integer division and modulo operators.'''

total_seconds = int(input("Enter time in seconds : "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")

'''Q3.Multiplication Table Generator

Problem:
Write a program that generates the multiplication table for a given number. 
The user should input a number, and the program will output its multiplication table from 1 to 10.'''

num = int(input("Enter the number for which you want the table: "))

for i in range(1, 11):
    result = num * i
    print(f"{num} * {i} = {result}")


'''Q4.Fibonacci Sequence

Problem:
Write a Python program that generates the first n Fibonacci numbers, where n is provided by the user. 
The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers. 
The program should output the sequence as a list. '''

num = int(input("Enter the number of Fibonacci numbers you want: "))

if num <= 0:
    print("Please enter a positive integer.")
elif num == 1:
    print([0])
elif num == 2:
    print([0, 1])
else:
    fibonacci_sequence = [0, 1]

    for i in range(2, num):
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)

    print(fibonacci_sequence)

'''Q5.Currency Converter

Problem:
Write a program that converts an amount in INR (Indian Rupees) into USD and GBP (user input) based on fixed conversion rates. Assume the conversion rates are as follows:

1 INR = 1 / 83.00 USD

1 INR = 1 / 103.00 GBP

The program should output the equivalent amount in USD and GBP for the entered INR.
You may assume that the user will enter valid numeric input.'''

inr = float(input("Please enter the amount in Indian Rupees: "))

usd = round(inr / 83.00, 2)
gbp = round(inr / 103.00, 2)

print(f"The Amount {inr} INR is {usd} USD")
print(f"The Amount {inr} INR is {gbp} GBP")

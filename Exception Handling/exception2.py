'''Q2. Safe Division with Multiple Exceptions

Problem:
Write a function safe_divide(a, b) that:

Divides two numbers a and b.

Handles the following exceptions:

ZeroDivisionError: print "Cannot divide by zero!"

ValueError: if the inputs cannot be converted to floats.

Any other exception: print "Unexpected error occurred!".

Use a loop to allow the user to keep entering numbers until they enter "exit".'''


def safe_divide(a, b):
    return float(a) / float(b)


print("Enter 'exit' if you want to exit the program")

while True:
    try:
        numerator = input("Enter numerator: ")
        if numerator.lower() == "exit":
            print("Exited the program")
            break

        denominator = input("Enter denominator: ")
        result = safe_divide(numerator, denominator)
        print(f"Result: {result} \n")

    except ValueError:
        print("Invalid input! Please enter numbers only.")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except Exception:
        print("Unexpected error occurred!")

'''Q1. Enhanced Calculator with String Formatting

Concepts Tested: Variables, Data Types, Operators, Control Structures, Casting, String Manipulation, String Formatting
Problem:
Write a Python program that asks the user for two numbers (as strings) and performs the following operations: addition, subtraction, multiplication, and division. Each result should be displayed in a formatted string, indicating which operation was performed. Ensure that the numbers are correctly cast to the appropriate numeric data types before performing the operations. Handle division by zero gracefully.

Additionally, use string formatting to present the results'''

num1 = input("Enter first number : ")
num2 = input("Enter second number : ")

sum = int(num1) + int(num2)
diff = int(num1) - int(num2)
prod = int(num1) * int(num2)
div = float(num1) / float(num2)

print("")
print(f"Sum of {num1} and {num2} is {sum}")
print(f"Difference of {num1} and {num2} is {diff}")
print(f"Product of {num1} and {num2} is {prod}")
print(f"Division of {num1} and {num2} is {div}")


'''Q2. Sentence Analysis - Word Count and Length

Concepts Tested: Variables, Data Types, Operators, Control Structures, String Manipulation, String Methods
Problem:
Create a Python program that asks the user for a sentence (string) and:

Counts the number of words in the sentence.

Finds the length of the longest word.

Finds the shortest word.

You should handle edge cases such as multiple spaces between words.'''

'''Q2. Sentence Analysis - Word Count and Length

Concepts Tested: Variables, Data Types, Operators, Control Structures, String Manipulation, String Methods
Problem:
Create a Python program that asks the user for a sentence (string) and:

Counts the number of words in the sentence.

Finds the length of the longest word.

Finds the shortest word.

You should handle edge cases such as multiple spaces between words.'''

sent = input("Enter a sentence : ")
words = sent.strip().split()

if not words:
    print("Please enter something. You have not entered any word")

count = len(words)

longest = words[0]
shortest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word
    elif len(word) < len(shortest):
        shortest = word
print("")    
print(f"Number of words in the sentence : {count}")
print(f"Longest word in the sentence : {longest} - {len(longest)} letters")
print(f"Shortest of word in the sentence : {shortest} - {len(shortest)} letters")

'''Q3. String Conversion and Comparison

Concepts Tested: Variables, Data Types, Operators, Control Structures, String Manipulation, String Casting, Comparison
Problem:
Write a Python program that:

Accepts two string inputs.

Converts both strings to lowercase and compares whether they are identical (ignoring case).

If they are not identical, the program should return the difference between the two strings (i.e., what characters are different and where).

Use string methods like lower(), strip(), and comparison operators to handle the task.'''


string1 = input("Enter the first string : ")
string2 = input("Enter the second string : ")
print("")
if string1.lower() == string2.lower():
    print("Both the strings are same ignoring the case")
else:
    print("The strings are not same. Here's the difference:")
    max_len = max(len(string1), len(string2))
    for i in range(max_len):
        if i >= len(string1):
            print(f"Position {i}: '{string2[i]}' is in the second string, but missing in the first string.")
        elif i >= len(string2):
            print(f"Position {i}: '{string1[i]}' is in the first string, but missing in the second string.")
        elif string1[i] != string2[i]:
            print(f"Position {i}: '{string1[i]}' (first string) vs '{string2[i]}' (second string)")


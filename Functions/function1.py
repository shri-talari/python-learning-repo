'''Q1. List Operations with Functions

Problem:
Write a function list_operations(numbers) that:

Takes a list of integers as input.

Returns a tuple containing:

The largest number

The smallest number

The sum of all numbers

A new set containing only unique even numbers'''


def list_operations(numbers):
    if not numbers:
        return (None, None, 0, set())

    total = 0
    smallest = numbers[0]
    largest = numbers[0]
    unique_evens = set()

    for num in numbers:
        total += num
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
        if num % 2 == 0:
            unique_evens.add(num)

    return (largest, smallest, total, unique_evens)


input_string = input(
    "Enter list of integers separated by space: ").strip().split()
integers_list = [int(x) for x in input_string if x != ""]
result = list_operations(integers_list)

print(f"Largest number : {result[0]}")
print(f"Smallest number: {result[1]}")
print(f"Sum of all numbers: {result[2]}")
print(f"Unique even numbers: {result[3]}")

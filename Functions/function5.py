'''Q5. Unique Elements Across Collections

Problem:
Write a function unique_elements(data1, data2) that:

Takes a tuple and a list as input.

Combines them into a single set of unique elements.

Returns both the set and its length.'''


def unique_elements(data1, data2):
    set1 = set(data1)
    set2 = set(data2)
    unique_set = set1 | set2
    length = len(unique_set)
    return unique_set, length


data1 = (1, 2, 3, 4, 2, 3)
data2 = [3, 4, 5, 6, 6]

output_set, length = unique_elements(data1, data2)
print(f"Set of unique elements combining both: {output_set}")
print(f"Length of set: {length}")

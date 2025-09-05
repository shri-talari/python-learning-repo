'''Q1. Unique Word Extractor

Input: A sentence string.

Task:

Convert to lowercase, split into words.

Store all unique words in a set.

Print count of unique words and the set itself (unordered).

Example: "This is a test this IS only a test"'''

sentence = input("Enter a Sentence : ").strip()
words = sentence.lower().split()
unique = set(words)

print(f"Count of unique words : {len(unique)} \n All Unique words in the sentence : {unique}")


'''Q2. Word Comparison Between Two Sentences

Input: Two sentences.

Task:

Create sets of words for each.

Print:

Common words (intersection)

Words only in first sentence

Words only in second sentence

Total unique words across both'''

sentence1 = input("Enter First Sentence : ").strip()
sentence2 = input("Enter Second Sentence : ").strip()

words1 = set(sentence1.lower().split())
words2 = set(sentence2.lower().split())

common = words1.intersection(words2)
first = words1.difference(words2)
second = words2.difference(words1)
total = words1.union(words2)

print(f"""Common Words : {common} 
      Words only in first sentence : {first}
      Words only in second sentence : {second}
      Total Unique words across both : {total}""")

'''Q3. Duplicate Remover from Mixed Data

Input: A tuple with duplicates: ("10", 20, "20", 30, "10", 40, 20, "30")

Task:

Convert all items to integers.

Store unique values in a set.

Convert back to a sorted list and print it.'''

input_tuple = ("10", 20, "20", 30, "10", 40, 20, "30")

integers = [int(x) for x in input_tuple]
unique = set(integers)
sorted_list = sorted(list(unique))

print(f"This is sorted list with only unique values : {sorted_list}")
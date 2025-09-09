'''Q3. Unique Word Counter with Error Handling

Problem:
Write a program that takes a sentence as input, splits it into words, and counts the frequency of each unique word using a dictionary.

Handle the case when the user inputs an empty string (ValueError).

Handle numbers inside the sentence by converting them to strings and still counting.

Ignore punctuation marks.'''


def unique_word_counter(sentence):
    punctuation = ".,!?;:'\"()-"
    for p in punctuation:
        sentence = sentence.replace(p, "")

    words = sentence.split()
    word_counts = {}

    for word in words:
        word = word.lower().strip()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


try:
    sentence = input("Enter a sentence: ").strip()
    if not sentence:
        raise ValueError("Input cannot be empty!")

    counts = unique_word_counter(sentence)

    print("\nWord Frequencies:")
    for word, count in counts.items():
        print(f"{word} : {count}")

except ValueError as e:
    print(f"Error: {e}")
except Exception:
    print("Unexpected error occurred!")

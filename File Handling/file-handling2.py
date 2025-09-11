'''Q2. Word Frequency Counter (File Version)

Problem:
Write a program that:

Reads a text file.

Cleans punctuation and splits into words.

Stores word frequencies in a dictionary.

Displays:

Top 5 most frequent words.

Unique word count.

Handle exceptions:

File not found.

Empty file.'''


try:
    with open("Files\\file2.txt", "r") as f:
        content = f.read()

        if not content.strip():
            print("File is empty!")
        else:
            punctuation = ".,':;/\\?\"!@#$%^&*()-_+=[]{}<>|`~"
            cleaned_content = ""
            for ch in content:
                if ch not in punctuation:
                    cleaned_content += ch.lower()
            words = cleaned_content.split()
            word_freq = {}
            for word in words:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1

            items = list(word_freq.items())
            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    if items[j][1] > items[i][1]:
                        items[i], items[j] = items[j], items[i]

            print("Top 5 Most Frequent Words:")
            top_n = 5 if len(items) >= 5 else len(items)
            for i in range(top_n):
                print(f"{items[i][0]}: {items[i][1]}")

            print(f"Unique Word Count: {len(word_freq)}")

except FileNotFoundError:
    print("File does not exist!")

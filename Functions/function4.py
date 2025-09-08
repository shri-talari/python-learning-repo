'''Q4. Word Frequency Counter

Problem:
Write a function word_frequency(sentence) that:

Takes a string sentence.

Returns a dictionary with each word as the key and its frequency as the value.

Ignore case (treat "Hello" and "hello" as the same).'''


def word_frequency(sentence):
    words = sentence.lower().split()
    return {word: words.count(word) for word in set(words)}


sentence = input("Enter a sentence: ").strip()
output = word_frequency(sentence)
print(output)

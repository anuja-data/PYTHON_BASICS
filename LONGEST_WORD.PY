# 3. Write a Python program to take a sentence from the user, split it into words, store them in a list, and print the longest word.

sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Find the longest word
longest = max(words, key=len)

print("List of words:", words)
print("Longest word:", longest)
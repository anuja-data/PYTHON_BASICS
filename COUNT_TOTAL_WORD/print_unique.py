# 1.Print the total number of words.

file = open("data.txt", "r")

content = file.read()

# Split the content into words
words = content.split()

# Find unique words
unique_words = set(words)

print("Unique words:", unique_words)
file.close()
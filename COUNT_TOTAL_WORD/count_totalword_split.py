# 4. Write a Python program to read a file, split its content into words, and store them in a list.

file = open("data.txt", "r")

# Read the content of the file
content = file.read()

# Split the content into words
words = content.split()

print("List of words:", words)

file.close()

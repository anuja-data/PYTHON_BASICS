# 2. Print all unique words.

file = open("data.txt", "r")

content = file.read()

# Split the content into words
words = content.split()

print("Total number of words:", len(words))

file.close()
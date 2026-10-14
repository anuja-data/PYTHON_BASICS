# 1. Write a program to read a file and count how many vowels are present in its content.

file = open("data.txt", "r")

# Read the content of the file
content = file.read()

# Count the vowels
count = 0
for ch in content:
    if ch.lower() in "aeiou":
        count = count + 1

print("Total number of vowels:", count)

file.close()
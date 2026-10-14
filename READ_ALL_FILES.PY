# 2. Write a Python program to read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th lines.

file = open("data.txt", "r")

# Read all lines into a list
lines = file.readlines()

# Print the total number of lines
print("Total number of lines:", len(lines))

if len(lines) >= 4:
    print("2nd line:", lines[1].strip())
    print("4th line:", lines[3].strip())
else:
    print("The file has fewer than 4 lines.")

file.close()
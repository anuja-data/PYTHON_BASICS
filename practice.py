# 1. Print sum of first 10 even numbers

numbers = [1, 7, 4, 7, 83, 3, 9, 2, 7, 100, 27, 36, 17, 34, 98, 56, 24, 22, 29, 12]

total = 0
count = 0

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        total = total + numbers[i]
        count = count + 1

        if count == 10:
            break

print("Sum of first 10 even numbers:", total)


# 2. Accept two values S and N.
#    Print square of first N numbers starting from S

S = int(input("Enter S: "))
N = int(input("Enter N: "))

for i in range(S, S + N):
    print(i * i)


# 3. Reverse the accepted string

string = input("Enter a string: ")

print("Reversed string:", string[::-1])


# 4. Accept sentence from user and count the vowels

sentence = input("Enter a sentence: ")

count = 0

for ch in sentence:
    if ch.lower() in "aeiou":
        count = count + 1

print("Number of vowels:", count)


# 5. Remove duplicates from list

numbers = [1, 2, 3, 2, 4, 1, 5, 3]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List after removing duplicates:", unique)


# 6. Reverse the list

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print("Reversed list:", numbers)

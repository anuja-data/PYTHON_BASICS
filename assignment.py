# 1. Create a list of 10 numbers and display the sum of last 4 elements.
li = [10, 20, 30, 40, 50, 80, 70, 70, 100, 90]

print("Sum of last four elements =", sum(li[-4:]))


# 2. Remove the items from the list located at 2nd and 5th position.
li.pop(1) 
li.pop(3)   
print("List after removing 2nd and 5th elements =", li)


# 3. Print the difference between the highest and smallest number of the list.
print("Difference between highest and smallest =", max(li) - min(li))


# 4. Append a new element which is half of the item located at 3rd position.
li.append(li[2] / 2)
print("Final list =", li)

# S="ababkejdb"
# arr=[0]*26
# for i in range(len(arr)):
#     print(chr(i+97))


S = "ababkejdb"
arr = [0] * 26

for ch in S:            #for i in range(len(a)):
    arr[ord(ch) - 97] += 1

for i in range(len(arr)):
    # if arr[i] > 0:
        print(chr(i + 97),"->", arr[i])
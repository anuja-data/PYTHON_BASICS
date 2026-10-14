# # 1.print tables of all odd no from 1 to 10
# NO=int(input("ENTER A NO 1 to 10:"))
# for i in range(1,11):
#     if NO % 2 !=0:
#         print("THE TABLES OF NO of ODD:",NO*i)



# # # 2.create a heterogenous list of no and names.split the list of no from highest number
# l=[23,"abc",893,"whfg",832964,"GVYGVU",377]
# num=[]
# name=[]
# for i in l:
#     if type(i)==int:
#         num.append(i)
#     else:
#         name.append(ijk)




# # 3.Accept the name and check if its palindrome

# NAME=input("ENTEE A NAME: ")
# if NAME.lower() == NAME.lower()[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")



# # 4.print the sum of digits

# NUMBER=int(input("ENTER A NUMBER:"))
# sum=0
# for i in range(NUMBER):
#     sum+=1
#     print("SUM OF NUMBERS",sum)


# # 5.print following pattern

# for i in range(1,6):
#     for j in range(1,i+1):
#         if i % 2==0:
#             print("#",end=" ")
#         else:
#             print("*",end=" ")
#     print()
    
    
    # 6.pyramid pattern

for i in range(1,6):
    for j in range(1,7-i):
        print("*",end=" ")
        for k in range(1,6+i):
                print(" ",end=" ")
print()
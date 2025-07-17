Number1=int(input("Enter the size of first List:"))
Number2=int(input("Enter the size of second List:"))

# while True:
list1=sorted(list(map(int,input().split())))
#     if len(list1)!=Number1:
#         continue
#     else:
#         break

# while True:
list2=sorted(list(map(int,input().split())))
#     if len(list2)!=Number1:
#         continue
#     else:
#         break

# list1=sorted(list1)
# list2=sorted(list2)
missing_list=[]

# # for i in range(len(list1)):
# #     for j in list2:

# #         if list1[i]==j:
# #             continue
# #         elif list1[i]!=j:
# #             missing_list.append(i)
            

# #     missing_list.extend(list1[i+1::])
# #     break
# # print(missing_list)

# for i in list1:
#     for j in list2:
#         # if list1.index(i)==len(list1):
#         #     missing_list.append(i)
#         if i ==j:
#             continue
#         else:
#             j=j+1
#             missing_list.append()
# print(missing_list)

 
# for i in list1:
#     if i not in list2:
#         missing_list.append(i)

# print(missing_list)

for i in range(0,len(list1)):
    # for j in range(0,len(list2)):
        if list1[i] not in list2:
            missing_list.append(list1[i])
# print(missing_list)
missing_list_set=set(missing_list)
print(missing_list_set)
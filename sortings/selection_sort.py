input_size=int(input("enter the input size:"))
list1=list(map(int,input().split(",")))

for i in range(0,len(list1)):
    min=i
    for j in range(i+1,len(list1)):
        if list1[j]<list1[min]:
            min=j
    
    list1[i],list1[min]=list1[min],list1[i]

print(list1)

# for i in range(0,len(list1)):
#     sorted=True
#     min=i
#     for j in range(i+1,len(list1)):
#         if list1[j]<list1[min]:
#             min = j
#             sorted=False
#         list1[i],list1[min]=list1[min],list1[i]
#     if(sorted):
#         break
# print(list1)
    # 45,32,7,3,473,57
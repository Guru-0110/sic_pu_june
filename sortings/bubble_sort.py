input_size=int(input("enter the input size:"))
list1=list(map(int,input().split(",")))

for i in range(0,len(list1)-1):
    for j in range(0,len(list1)-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)
#  exact no of comparisions = n(n-1)/2
# worst case = n(n-1)/2


# # Optimized code
#  exact no of comparisions = n-1
# worst case also the comparisions = n-1
# input_size=int(input("enter the input size:"))
# list1=list(map(int,input().split(",")))

# for i in range(0,len(list1)-1):
#     sorted=True
#     for j in range(0,len(list1)-i-1):
#         if list1[j]>list1[j+1]:
#               list1[j],list1[j+1]=list1[j+1],list1[j]
#               sorted=False
#     if(sorted):
#         #  print("Elements are already sorted")
#          break
# print(list1)

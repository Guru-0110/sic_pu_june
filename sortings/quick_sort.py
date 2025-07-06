number=int(input("enter the number of inputs to be given into the list:"))
list1=[]
for i in range(number):
    list1.append(int(input()))
# print(list1)

low=0
high=len(list1)-1

def quick_sort(list1,low,high):
    if low<high:
        pivot_index=partition(list1,low,high)
        quick_sort(list1,low,pivot_index-1)
        quick_sort(list1,pivot_index+1,high)
    return list1

# def partition(list1,low,high):
#     pivot=list1[high]
#     k=low
#     for i in range(low,high):
#         if list1[i]<pivot:
#             list1[i],list1[k]=list1[k],list1[i]
#             k +=1
#     list1[high],list1[k]=list1[k],list1[high]
#     return k





def partition(list1,low,high):
    pivot=list1[low]
    k=high
    for i in range(low,high+1):
        if list1[i]>pivot:
            list1[i],list1[k]=list1[k],list1[i]
            k-=1
    list1[low],list1[k]=list1[k],list1[low]
    return k

print(quick_sort(list1,low,high))



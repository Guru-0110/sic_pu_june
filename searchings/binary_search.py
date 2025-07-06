# list1=list(map(int,input().split()))
# target = int(input("Enter the Element to be found:"))
# sorted_list=sorted(list1)
# low=0
# high=len(sorted_list)-1

# while low<=high:
#         mid=(high+low)//2
#         if sorted_list[mid] == target:
#             print(f"Element found at {mid}")
#             break
#         elif target>sorted_list[mid]:
#             low=mid+1
#         else:
#             high=mid-1


# Recursively

def Binary_search(high,low,target):
    if high<low:
        return "Element not found"
    mid=(high+low)//2
    if sorted_list[mid]==target:
        return f"Found at position {mid}"
    elif target>sorted_list[mid]:
        return Binary_search(high,mid+1,target)

    else:
        return Binary_search(mid-1,low,target)


list1=list(map(int,input().split()))
target = int(input("Enter the Element to be found:"))
sorted_list=sorted(list1)
low=0
high=len(sorted_list)-1
print(Binary_search(high,low,target))
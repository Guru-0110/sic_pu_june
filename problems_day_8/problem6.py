size_of_list=int(input("Enter the size of the list:"))
# list_elements =list(map(int,input().split()))
print("Enter the list of elements")
list_elements=[]
for i in range(size_of_list):
    list_elements.append(int(input()))

Number_of_instructions=int(input("Provide the number of instructions Needed:"))
Target_element=int(input("Provide the target element:"))

list1=[]
i=0
while i<Number_of_instructions:
    string_input=input()

    if string_input=="harry":
        Harry_value=list_elements.pop(0)
        list1.append(Harry_value)
    elif string_input =="remove":
        list1.pop()
    i+=1
sum_list=sum(list1)
if sum_list==Target_element:
        print(len(list1))
        

        
# list1=[1,2,3,4]
# target=3
# list2=[]
# print(len(list1))
# for i in range(1,4):
#     if list1[i-1]+list1[i]==target:
#         list2.append(list1[i-1])
#         list2.append(list1[i])
    
# print(list2)
list1=[0,1,2,3,4]
target=5
list2=[]
print(len(list1))
for i in range(1,4):
    if list1[i-1]+list1[i]==target:
        list2.append(list1[i-1])
        list2.append(list1[i])
    
print(list2)
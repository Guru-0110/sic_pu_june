Number_of_oranges=int(input("Enter the Number of oranges picked:"))
list1=list(map(int,input().split()))
k=0
last_orange=len(list1)
for i in range(0,last_orange):
    if list1[i]<=list1[last_orange-1]:
        list1[i],list1[k]=list1[k],list1[i]
        k+=1
list1[k],list1[len(list1)-1]=list1[len(list1)-1],list1[k]

print(list1)
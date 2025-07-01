# # 1. Find smallest and biggest elements in an list of n numbers.


# # list1=list(map(int,input("Enter the list elements:").split(",")))
# # maximum=max(list1)
# # minimum=min(list1)
# # print(f"The Maximum Number is :{maximum}")
# # print(f"The Manimum Number is :{minimum}")



# # 2. Find the frequency an element in a list of n elements.



# list2=list(map(int,input("Enter the list elements:").split(",")))
# number=int(input("Enter the Number to find its frequency on the list:"))
# count=0
# for i in list2:
#     if number==i:
#         count=count+1
# print(f"the number {number} is repeated {count} number of times")


# # 3. Remove the duplicates in a list of size n



# list3=list(map(int,input("Enter the list elements:").split(",")))
# Non_duplicated_list=[]
# for i in list3:
#     if i not in Non_duplicated_list:
#         Non_duplicated_list.append(i)
# print(Non_duplicated_list)



# 4. Given a number, find very next possible bigger number that has all the digits of the given number.

# list1=[1,2,3]
# list2=[]
# list2.extend(list1)


# Number=input("Enter the number:")
# list1=list(Number)
# list2=[]
# for i in range(0,len(list1)):
#     list2.append(list1[i])
# list3=[].extend(list2)
# number1=''.join(list3)
# print(number1)


Number=input("Enter a Digit:")
list1=list(Number)
list2=[]
for i in range(0,len(list1)):
    list2.append(list1[i])
    if i == len(list1)-1:
        list2.append(str(int(list1[i])+1))
Number2=''.join(list2)
print(f"The Number which is greater than {Number} is  {Number2}")
    
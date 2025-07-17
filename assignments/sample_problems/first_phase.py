# Number_input=int(input("Enter the size of the array:"))

# N_elements=[]
# for i in range(1,Number_input):
#     N_elements.append(i)


# p_elements=[]
# for i in range(1,100):
#     p_elements.append(i)
# X=[]
# Y=[]


# counter_for_p=0
# for i in p_elements:
#        for a in N_elements:
#            if a>i:
#                X.append(a)
#                counter_for_p+=1
#            else:
#                Y.append(a)
       
Number_input=int(input("Enter the size of the list:"))
first_phase=int(input("Enter the first element:"))
last_phase=int(input("Enter the last phase:"))

List_input=list(map(int,input().split(",")))

sorted_list=sorted(List_input)
first_element=sorted_list[first_phase-1]
second_element=sorted_list[first_phase]
count =0 
for i in range(first_element,second_element-1):
    count+=1
print(count)
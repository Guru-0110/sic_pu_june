Number_of_requestes=int(input("Enter the Number of requestes:"))
requests_recieved=[]
for i in range(-5,Number_of_requestes,1):
    requests_recieved.append(i)

# print(server1)

# memory_allocation=[]
# memory_deallocation=[]

# for i in server1:
#     if i<=0:
#         memory_deallocation.append(i)
#     else:
#         memory_allocation.append(i)
# print(memory_allocation)
# print(memory_deallocation)
server1_at_Even_locations=[]
for i in range(0,len(requests_recieved)):
    if i%2==0:
        server1_at_Even_locations.append(i)
print(server1_at_Even_locations)
print(sum(server1_at_Even_locations))
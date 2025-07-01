import sys

# print("Hello")
# print(sys.argv)
list1=sys.argv[1:]
# for i in sys.argv(1,len(sys.argv))
# print(list1)
list2=[]
for i in list1:
    list2.append(i.split())
# print(list2)
states=[]
capitals=[]
for i in list2:
    for j in range(0,1):
        states.append(i[j])
        capitals.append(i[j+1])

print('%-15s %s' % ('STATE', 'CAPITAL'))
print('-' * 24)
for i in range(len(states)):
    print('%-15s %s' % (states[i], capitals[i]))

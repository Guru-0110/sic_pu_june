# list1=list(map(int,input().split(",")))
# removed_list=[]
# for i in range(len(list1),0,-1):
#     list1.remove(i)
#     print(list1)
import sys

class stack():
    
    def __init__(self,size):
        self.top=-1
        self.size=size
        self.stack=[]
    def is_empty(self):
        if self.top == -1:
            print("The stack is empty")
    def is_full(self):
        if self.top==self.size:
            print("The stack is full")
    def pop(self):
        if self.top==-1:
            print("The stack is empty")
        else:
            self.stack.pop()
            self.top = self.top-1
            print(f"The element popped ")
    def push(self,value):
        self.value = value
        if self.top==self.size:
            print("The stack is full")
        else:
            self.stack.append(value)
            self.top=self.top+1
            print(f"{value} inserted into the stack")
    def display(self):
        print(self.stack)

    def invalid_choice(self):
        print("invalid input!!")
    
    def exit_order(self):
        exit("end of program")
size_of_stack=int(input("enter the size of the stack:"))
object1=stack(size_of_stack)
menu={
    1:object1.push,
    2:object1.pop,
    3:object1.display,
    4:object1.exit_order
    }
# stack_obj=stack(5)
# stack_obj.push(1)
# stack_obj.display()
# stack_obj.push(4)
# stack_obj.display()
# stack_obj.push(3)
# stack_obj.display()
# stack_obj.push(2)
# stack_obj.display()

# stack_obj.pop()
# stack_obj.pop()
# stack_obj.pop()

# stack_obj.display()
# object2=len(object1.stack)
# print(object2)

print("1.push, 2.pop, 3.display, 4.Exit")
while True:
    input_=int(input(("enter the choice:")))
    if input_==1:
        input_for_push=input("Enter the item to be pushed:")
        menu.get(input_)(input_for_push)
    else:
        menu.get(input_,object1.invalid_choice)()
  
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
    def delete(self):
        if self.top==-1:
            print("The stack is empty")
        else:
            self.stack.pop(0)
            self.top = self.top-1
            print(f"The element popped from the position 0")
    def insert(self,value):
        self.value = value
        if self.top==self.size:
            print("The stack is full")
        else:
            self.stack.insert(0,value)
            self.top=self.top+1
            print(f"{value} inserted into the stack at the position 0")
    def display(self):
        print(self.stack)

    def invalid_choice(self):
        print("invalid input!!")
    
    def exit_order(self):
        exit("end of program")
size_of_stack=int(input("enter the size of the stack:"))
object1=stack(size_of_stack)
menu={
    1:object1.insert,
    2:object1.delete,
    3:object1.display,
    4:object1.exit_order
    }

print("1.push, 2.pop, 3.display, 4.Exit")
while True:
    input_=int(input(("enter the choice:")))
    if input_==1:
        input_for_push=input("Enter the item to be pushed:")
        menu.get(input_)(input_for_push)
    else:
        menu.get(input_,object1.invalid_choice)()
class queue:
    def __init__(self,size):
        self.size=size
        self.rear=-1
        self.front=-1
        self.queue=[]
    def empty_queue(self):
        if self.front==-1 and self.rear==-1:
            print("The queue is empty")
    def full_queue(self):
        if self.front==self.size:
            print("The Queue is Full")
    def enqueue(self,value):
        if self.front==self.size:
            print("The queue is full")
        else:
            self.queue.append(value)
            self.front+=1
    def dequeue(self):
        if self.rear==-1:
            print("The queue is empty")
        else:
            self.queue.pop(0)
            print(f"The element removed is :{self.queue.pop(0)}")
            self.rear+=1
        

    def display(self):
        print(self.queue)
    
    def invalid_choice(self):
        print("Invalid choice")

    def exit(self):
        exit("End of program!!")

Size_of_queue=int(input("Enter the size of the queue:"))
obj=queue(Size_of_queue)

menu={
    1:obj.enqueue,
    2:obj.dequeue,
    3:obj.display,
    4:obj.exit
}
print("1.enqueue, 2.dequeue, 3.display,4.exit:")
while True:
    input_=int(input(("enter the choice:")))
    if input_==1:
        input_for_push=input("Enter the item to be pushed:")
        menu.get(input_)(input_for_push)
    else:
        menu.get(input_,obj.invalid_choice)()

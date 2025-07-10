class list:

    class Node:
        def __init__(self,value):
            self.value=value
            self.next = None
    
    class Linked_list():
        def __init__(self):
            self.head =None

        def insert_at_begining(self,value):
            new_node = list.Node(value)
            new_node.next = self.head
            self.head = new_node

        def delete_at_begining(self):
            if self.head == None:
                print("The list is empty:")
            else:
                self.head = self.head.next
                
        def display(self):
            temp = self.head
            while temp:
                print(temp.value ,"--->",end ="")
                temp=temp.next

    def __init__(self):
         self.list = self.Linked_list()

    def push(self,value):
        self.list.insert_at_begining(value)
    
    def pop(self):
        self.list.delete_at_begining()

    def diplay_for_list(self):
        self.list.display()
    
obj1 = list()
obj1.push(2)
obj1.push(4)
obj1.push(6)
obj1.pop()
obj1.diplay_for_list()
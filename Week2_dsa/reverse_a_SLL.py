class Node:
    def __init__(self,value):
        self.value = value
        self.next= None

class singly_Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self,value):
        new_node = Node(value)
        temp = self.head
        while temp.next != None:
            temp=temp.next
        temp.next=new_node
        # new_node.next=None
    
   
    def insert_at_position(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            count = 0
            while temp is not None and count < position - 1:
               temp = temp.next
               count += 1
        if temp is None:
            print("Position out of range.")
        else:
            new_node.next = temp.next
            temp.next = new_node

    def delete_at_begining(self):
        if self.head == None:
            print("The Linked list is empty:")
        else:
            self.head = self.head.next
    def delete_at_end(self):
        if self.head == None:
            print("The Linked list is empty:")
        else:
            temp=self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
    def delete_at_position(self,position):
        if self.head == None:
            print("The Linked list is empty:")
        else:
            temp = self.head
            for _ in range(position):
                temp = temp.next
            temp.next = temp.next.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.value,"-->",end="")
            temp=temp.next
    
    def reverse_of_SLL(self,node):
        if node == None:
            return 
        self.reverse_of_SLL(self.node.next)
        print(self.node.value)

obj1=singly_Linked_list()
obj1.insert_at_begining(2)
obj1.insert_at_begining(4)
# obj1.insert_at_end(6)
obj1.insert_at_position(8,1)
obj1.display()
obj1.reverse_of_SLL(obj1.node.head)



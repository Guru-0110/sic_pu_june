class queue:

        class Node:
          def __init__(self,value):
            self.value = value
            self.next = None

        class Linked_list:
           def __init__(self):
               self.head = None
    
           def insert_at_begining(self,value):
                new_node = queue.Node(value)
                new_node.next = self.head
                self.head=new_node

           def insert_at_end(self,value):
            new_node=queue.Node(value)
            if self.head is None:
                self.head = new_node
                return
            else:
               temp = self.head
               while temp.next != None:
                  temp = temp.next
               temp.next= new_node

            def insert_at_position(self,value,position):
              new_node = queue.Node(value)
              if position==0:
                new_node.next=self.head
                self.head=new_node
              elif position==1:
                temp=self.head
                for _ in range(2):
                      temp=temp.next
                new_node.next=temp.next
                temp.next=new_node


              else:
                temp = self.head
                for _ in range(1,position):
                   temp = temp.next
                new_node.next=temp.next
                temp.next=new_node

           def delete_at_begining(self):
            if self.head==None:
               print("No elements present")
            else:
              self.head = self.head.next

            def delete_at_end(self):
             if self.head ==None:
                print("No elements")
             elif self.head.next==None:
                self.head = None
             else:
                temp = self.head
             while temp.next.next !=None:
                temp=temp.next
             temp.next=None
           def delete_at_position(self,position):
            if position==0:
               self.head = self.head.next
            elif position==1:
               temp=self.head
               temp=temp.next.next
            else:
               temp=self.head
               for _ in range(1,position):
                  temp=temp.next
               temp.next=temp.next.next

           def display(self):
            temp = self.head
            while temp:
              print(temp.value, " -> ",end="",)
              temp=temp.next
            print("\n")
            def reverse(self,node):
             if node==None:
                return
             self.reverse(self.node.next)
             print(self.node.value,"->",end="")

        def __init__(self):
           self.list=self.Linked_list()
         
        def enqueue(self,value):
         #   self.value=value
           self.list.insert_at_end(value)
         
        def dequeue(self):
           return self.list.delete_at_begining()
        def display1(self):
           self.list.display()
            
obj1=queue()
# obj1.insert_at_begining(1)
# obj1.insert_at_end(2)
# obj1.insert_at_end(3)
# obj1.insert_at_end(4)
# obj1.insert_at_end(5)
# obj1.delete_at_position(3)


# obj1.display()
# # obj1.reverse(obj1.head)
# obj1.enqueue()
# obj1.dequeue()
obj1.enqueue(1)
obj1.enqueue(3)
obj1.enqueue(5)
obj1.enqueue(7)
obj1.dequeue()
obj1.display1()


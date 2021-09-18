
##Iterative Method

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev =None
        current =self.head
        while(current is not None):
            temp = current.next
            current.next = prev
            prev = current
            current = temp       

        self.head = prev       

    def insert(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
llist = LinkedList()
llist.insert(20)                     
llist.insert(40)                                        
llist.insert(320)                     
llist.insert(520)                     
llist.insert(270)                     
llist.insert(220) 
llist.printList()                    
llist.reverse()
llist.printList()

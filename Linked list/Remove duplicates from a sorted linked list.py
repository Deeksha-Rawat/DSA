import math
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def remove(head):
    if(head == None and head.next==None):
        return
    p1 =head
    while(p1 and p1.next):
        if p1.data == p1.next.data:
            p1.next = p1.next.next

        else:
            p1 = p1.next
    return
def push(ref,new_data):
    new_node = Node(new_data)
    new_node.data = new_data
    new_node.next = ref

    ref = new_node

    return ref
def printlist(node):
    while(node):
        print(node.data,end=" ")
        node=node.next    


if __name__=='__main__': 
   
    head = None
     
    head = push(head, 20) 
    head = push(head, 13) 
    head = push(head, 13) 
    head = push(head, 11) 
    head = push(head, 11) 
    head = push(head, 11)                                 
   
    print("List before removal of " 
          "duplicates ", end = "") 
    printlist(head) 
   
    remove(head) 
   
    print("\nList after removal of " 
          "elements ", end = "") 
           
    printlist(head)                                            

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def newNode(data):
    temp = Node(data)
    return temp

def printList(head):
    while head:
        print(head.data,end=" ")
        head = head.next
    print()

def detectfirst(head):
    slow=head
    fast=head
    while(slow and fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return slow
            break
if __name__ == '__main__':
    head = newNode(50)
    head.next = newNode(20)
    head.next.next = newNode(15)
    head.next.next.next = newNode(4)
    head.next.next.next.next = newNode(10)  

            

    res = detectfirst(head)
    if res==None:
        print("no")
    else:
        print("yes")    




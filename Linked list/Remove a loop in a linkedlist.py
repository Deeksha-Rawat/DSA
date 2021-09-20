def detectloop(self):
    slow = fast = self.head
    while(slow and fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            self.removeloop(slow)
            return 1
    return 0

def removeloop(self,loopnode):
    ptr1 = loopnode
    ptr2 = loopnode

    k=1
    while(ptr1.next!=ptr2):
        k+=1
        ptr1=ptr1.next

    ptr1 = self.head
    ptr2 = self.head
    for i in range(k):
        ptr2 = ptr2.next
    while(ptr2!=ptr1):
        ptr1 = ptr1.next        
        ptr2 = ptr2.next 

    while(ptr2.next!=ptr1):
        ptr2 = ptr2.next

    ptr2.next=None
                   

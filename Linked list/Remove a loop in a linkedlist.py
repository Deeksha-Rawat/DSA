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
                   

        
        
        
 ###using hashing####

def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        if head == None or head.next == None:
            return
        p1=head
        prev = None
        h=set()
        while(p1):
            if p1 in h:
                
                prev.next = None
                return
            h.add(p1)
            prev = p1
            p1=p1.next

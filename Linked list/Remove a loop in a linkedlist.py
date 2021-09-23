 
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

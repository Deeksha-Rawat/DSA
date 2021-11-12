def findIntersection(a,b):
    #return head
    dummy = Node(0)
    tail = dummy
    dummy.next = None
    while(a!=None and b!=None):
        if a.data==b.data:
            tail.next = a
            tail=tail.next
            a=a.next
            b.next
            
        elif(a.data<b.data):
            a=a.next
        else:
            b=b.next
    return dummy.next

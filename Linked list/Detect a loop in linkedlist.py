def detectLoop(self, head):
        #code here
        
        slow=head
        fast= head
        while(slow and fast and fast.next):
            slow=slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False
      
      
      
      
###2nd method using set

a=set()
temp=head
while(temp):
    if temp in a:
        return True
    a.add(temp)
    temp=temp.next

return False
      
      

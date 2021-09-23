def removeduplicates(self,head):
  if head==None or head.next==None:
    return head
  current = head
  hash=set()
  hash.add(head.data)
  current =head
  while(current.next):
    if current.next.data in hash:
      current.next=current.next.next
    else:
      hash.add(current.next.data)
      current=current.next
  return head    
  

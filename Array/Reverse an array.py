1.  a = [1,2,3,4]
    print(a[::-1])


/////////////////
2.



def reverse(a,start,end):
  while(start<end):
    a[start],a[end]=a[end],a[start]
    reverse(a,start+1,end-1)
    
a = [1,2,3,4]
reverse(a,0,len(a)-1)
print(a)
    

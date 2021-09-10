1.  
a = [1,2,3,4]
print(a[::-1])


    
    
/////////////////
2.
def rev(a,start,end):
    if start>=end:
        return
    a[start],a[end] = a[end],a[start]
    rev(a,start+1,end-1)
    
a=[1,2,3]
rev(a,0,len(a)-1)
print(a)
    

a=[1, 3, 5, 5, 5, 5, 67, 123, 125 ]
n=9
x=5
b=[]
ans=[-1,-1]
for i in range(n):
    if a[i]==x:
        b.append(i)
if len(b)>0:
  ans=[b[0],b[-1]]
  print(ans)  
else:
  print(ans)
  
  
######using binary search######
  
  

             
""" first  """
def first(a,x,n):
    low=0
    high=n-1
    res =-1
    while(low<=high):
        mid = (low+high)//2
        if a[mid]>x:
            high=mid-1
        elif a[mid]<x:
            low=mid+1
        else:
            res = mid
            high =mid-1
    return res

def last(a,x,n):
    low=0
    high=n-1
    res=-1
    while(low<=high):
        mid=(low+high)//2
        if a[mid]>x:
            high=mid-1
        elif a[mid]<x:
            low=mid+1
        else:
            res=mid
            low=mid+1
    return res

a=[1, 3, 5, 5, 5, 5, 67, 123, 125 ]
n=9
x=5
print(first(a,x,n),last(a,x,n))                    





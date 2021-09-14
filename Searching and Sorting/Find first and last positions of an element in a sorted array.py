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
  
  

a=[15, 2, 45, 12, 7]
n=5
ans=[]
for i in range(n):
    if a[i] == i+1:
        ans.append(a[i])
if len(ans)==0:
  print("not found")
else:
  print(*ans)
  

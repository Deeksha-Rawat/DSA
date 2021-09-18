## 1st solution

a=[20, 40, 50, 70, 70, 60]
k=20
x=60
for i in range(len(a)):
    if a[i]==x:
        print(i)
        break
        
        
## 2nd solution (more optimized)
a=[2,4,5,6,8]
k=2
x=6
i=0
while(i<len(a)):
    if a[i]==x:
        print(i)
        break
        
    i = i + max(1, int(abs(a[i]-x)/k))





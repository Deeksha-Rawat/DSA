

a= [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n = len(a)


c0=0
c1=0
c2=0

for i in range(n):
    if a[i]==0:
        c0+=1
    if a[i]==1:
        c1+=1

    if a[i]==2:
        c2+=1
i=0
while(c0>0):
    a[i] = 0
    i+=1
    c0-=1
while(c1>0):
    a[i] = 1
    i+=1
    c1-=1
while(c2>0):
    a[i] = 2
    i+=1
    c2-=1                        
print(a)



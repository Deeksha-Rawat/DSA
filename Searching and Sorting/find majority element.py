a=[3,1,3,3,2]
hash ={}
n=5
count=0        

for i in a:
    if i in hash:
        hash[i]+=1
    else:
        hash[i]=1
for i in hash:
    if hash[i]>n//2:
        count=1
        print(i)
        break
if count==0:
    print(-1)
    

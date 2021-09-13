n=4
k=6
count=0
a = [1,5,7,1]
hash = {}
for i in range(n):
    s = k-a[i]
    if s in hash:
        count+=hash[s]
        print(hash)
    if a[i] in hash:
        hash[a[i]]+=1
    else:
        hash[a[i]] = 1        
print(count)        
 

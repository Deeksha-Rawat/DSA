###solution1###

a=[2,2,1,4,3]
n =len(a)
a.sort()
count=0
for i in range(1,n):
    if a[i]==a[i-1]:
        count+=1
        print(a[i])    

        
        
###solution2(more optimized)###

a=[2,2,1,4,3]
b = Counter(a)
res = b.most_common()[0][0]
print(res)

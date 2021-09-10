a = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

n=len(a)

j = 0
for i in range(n):
    if a[i] < 0:
        a[i],a[j] = a[j],a[i]
        j+=1
     
print(a)        

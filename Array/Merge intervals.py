a = [[1,3],[2,6],[8,10],[15,18]]

i = 0
j = 1

while(j<len(a)):
    f0 = a[i][0]
    f1 = a[i][1]
    l0 = a[j][0]
    l1 = a[j][1]

    if l0 <=f1<=l1 or l0 <= f0 <= l1 or f0<= l1<=f1:
        a[i][0] = min(f0,l0)   
        a[i][1] = max(f1,l1)

        del a[j]
    else:
        i+=1
        j+=1
print(a)       
        

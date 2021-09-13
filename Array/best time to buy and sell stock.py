a = [7,1,5,3,6,4]
max=0
for i in range(0,len(a)):
    for j in range(i,len(a)):
        s = a[j]-a[i]
        if max < s:
            max = s
print(max)

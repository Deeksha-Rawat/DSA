
a = [1,2,3,4,5]
n=len(a)
temp = a[n-1]
for i in range(n):
    a[n-i-1] = a[n-i-2]
a[0] = temp
print(a)


###########output#########

a = [5,1,2,3,4]

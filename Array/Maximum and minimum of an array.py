# using linear search
# time complexity - O(n)

def search(a,n):
    min = a[0]
    max = a[0]
    for i in range(n):
        if a[i]<min:
            min = a[i]
        if a[i]>max:
            max = a[i]
    return max,min

a=[1,4,2,5]
n = len(a)
print(search(a,n)) 



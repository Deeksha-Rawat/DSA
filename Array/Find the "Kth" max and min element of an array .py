# using bubble sort


def bubblesort(a,n):

    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

            
""" smallest = a[k-1]
largest = a[-k] """

a=[7, 10, 4, 3, 20, 15]
n = len(a)
k=3
bubblesort(a,n)
print(a[k-1],a[-k])   



# using sort()

a=[7, 10, 4, 3, 20, 15]
k=3
a.sort()
print(a[k-1],a[-k])  

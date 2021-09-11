##kadane's algorithm##

a = [-4,-5,-5,-3]
n = len(a)

currentsum = 0
maxsum = a[0]
for i in range(n):
    currentsum = max(a[i],currentsum+a[i])
    if currentsum > maxsum:
        maxsum = currentsum
print(maxsum)        

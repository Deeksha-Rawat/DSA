import heapq
class Solution():
    def mergeHeaps(self, a, b, n, m):
        #your code here
        
        for i in b:
            heapq.heappush(a,i)
        n=n+m
        for i in range(n-1//2,-1,-1):
            self.heapify(a,n,i)
        return a    
    def heapify(self,arr,n,i):
        largest = i
        l=2*i+1
        r=2*i+2
    
        if l<n and arr[largest]<arr[l]:
            largest = l 
        if r<n and arr[largest]<arr[r]:
            largest = r
        if largest!=i:
            a[largest],a[i]=a[i],a[largest]
            self.heapify(arr,n,largest) 

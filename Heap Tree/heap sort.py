class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,a, n, i):
        # code here
        largest = i 
        l=2*i+1
        r=2*i+2
        
        if l<n and a[l] >a[largest]:
            largest=l
        if r<n and a[r] >a[largest]:
            largest = r
        if largest!=i:
            a[i],a[largest]=a[largest],a[i]
            
            self.heapify(a,n,largest)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n-1//2,-1,-1):
            self.heapify(arr,n,i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        for i in range(n-1,0,-1):
            arr[i],arr[0] = arr[0],arr[i]
            self.heapify(arr,i,0)

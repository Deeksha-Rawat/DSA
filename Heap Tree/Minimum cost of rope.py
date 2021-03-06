import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n):
        # code here
        heapq.heapify(arr)
        
        res = 0 
        while(len(arr)>1):
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            
            res+=first+second
            
            heapq.heappush(arr,first+second)
        
        return res    
        

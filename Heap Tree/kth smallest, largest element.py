##leetcode solution

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        
        ans = nlargest(k,nums)
        return ans[k-1]
      
      
#for smallest
ans =nsmallest(k,nums)


##using priority queue
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap =[-int(x) for x in nums]
        for i in range(len(nums)):
            heapify(heap)
            for i in range(k-1):
                heappop(heap)
            return str(-heap[0]) 

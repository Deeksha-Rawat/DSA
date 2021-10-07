##leetcode solution

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        
        ans = nlargest(k,nums)
        return ans[k-1]
      
      
#for smallest
ans =nsmallest(k,nums)

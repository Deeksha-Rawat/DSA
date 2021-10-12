from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S: return "" 
        # create a counter 
        heap = []
        c=Counter(S)
        for key, value in c.items():
            heapq.heappush(heap,[-value,key])

        res = ""
        pre = heapq.heappop(heap)
        res+= pre[1]

        while heap: 
            curr = heapq.heappop(heap)
            res+=curr[1]

            pre[0]+=1
            if pre[0]<0:
                heapq.heappush(heap,pre)
            pre = curr 

        return "" if len(res)!=len(S) else res

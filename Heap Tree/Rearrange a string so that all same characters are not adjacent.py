#code
from collections import Counter
import heapq

def tocheck(s):
    
    res=""
    if s is None:
    
        return False
    c = Counter(s)
    heap = [(-value,key) for key,value in c.items()]
    while len(heap)>1:
        f1,c1 = heapq.heappop(heap)
        f2,c2 = heapq.heappop(heap)
        res+=c1
        res+=c2
    
        if abs(f1)>1:
            heapq.heappush(heap,(f1+1,c1))
            
        if abs(f2)>1:
            heapq.heappush(heap,(f2+1,c2))
    if heap:
        f0,c0 = heap[0]
        if abs(f0)>1:
            return False
        else:
            res+=c0
    return True
    
    
    
import sys

    
t=int(input())
for _ in range(t):
    
   
    s=str( sys.stdin.readline() )    
    
    r=tocheck(s)
    if r:
        print(1)
    else:
        print(0)
    
    
            
    
    

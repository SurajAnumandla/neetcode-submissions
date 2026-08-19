import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task,0)+1
        heap = []
        count = 0
        for val in freq.values():
            heapq.heappush(heap,(-val))
         
        q = deque()
        time = 0
        while heap or q:
            time+=1
            if heap:
                val= heapq.heappop(heap)
                if val+1 != 0:
                    q.append((val+1,time+n))
            if q and q[0][1] == time:
                heapq.heappush(heap,q.popleft()[0])
        return time

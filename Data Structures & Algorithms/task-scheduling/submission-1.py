import heapq
from collections import defaultdict
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for c in tasks:
            freq[c]+=1
        heap = []
        for val in freq.values():
            heapq.heappush(heap,-val)
        count = 0
        q = deque()
        while heap or q:
            count+=1
            if heap:
                val = heapq.heappop(heap)
                if val+1!=0:
                    q.append((val+1,count+n))
            if q:
                if q[0][1]==count:
                    heapq.heappush(heap,q.popleft()[0])
        return count


import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []

        for val in stones:
            heapq.heappush(h,-val)
        
        while len(h)>1:
            a = -heapq.heappop(h)
            b = -heapq.heappop(h)

            diff = a - b
            if diff!=0:
                heapq.heappush(h,-diff)
        
        return 0 if not h else -h[0]
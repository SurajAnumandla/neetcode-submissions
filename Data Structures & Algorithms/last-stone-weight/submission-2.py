import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        if len(stones)==1:
            return stones[0]

        for val in stones:
            heapq.heappush(heap,(-val))
        
        while heap:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x < y:
                w = y-x
                heapq.heappush(heap,-w)
            elif x > y:
                w = x-y
                heapq.heappush(heap,-w)
            if len(heap)==1:
                break
        return -heap[0] if heap else 0
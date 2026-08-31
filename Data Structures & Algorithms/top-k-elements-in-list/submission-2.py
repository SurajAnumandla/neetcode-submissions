from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for n in nums:
            seen[n]+=1
        heap = []

        for key,val in seen.items():
            heapq.heappush(heap,(val,key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [ val for key,val in heap]
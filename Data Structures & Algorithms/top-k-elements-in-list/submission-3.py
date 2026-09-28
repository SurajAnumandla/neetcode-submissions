import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for n in nums:
            res[n] = res.get(n,0)+1
        heap = []
        for v,c in res.items():
            heapq.heappush(heap,(c,v))
            if len(heap)>k:
                heapq.heappop(heap)
        return [v for c,v in heap]
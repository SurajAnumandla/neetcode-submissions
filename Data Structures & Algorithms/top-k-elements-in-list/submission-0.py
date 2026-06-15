import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dic = defaultdict(nums)
        dic = {}

        for val in nums:
            dic[val]= dic.get(val,0)+1
        
        heap = []
        for key,val in dic.items():
            heapq.heappush(heap,(val,key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [val[1] for val in heap]
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for val in nums:
            heapq.heappush(h,val)
            if len(h)>k:
                heapq.heappop(h)
        return h[0]
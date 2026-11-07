import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        if not points or not points[0]:
            return points
        heap = []

        for co in points:
            x = co[0]
            y = co[1]
            dist = math.sqrt((0-x)*(0-x) + (0-y)*(0-y))
            heapq.heappush(heap,(-dist,co))
            if len(heap)>k:
                heapq.heappop(heap)
        return [val[1] for val in heap]
        
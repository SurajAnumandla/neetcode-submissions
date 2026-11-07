"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        arr = sorted(intervals, key = lambda x: x.start)
        n = len(arr)
        heap = []
        heapq.heappush(heap,arr[0].end)
        for i in range(1,n):
            if arr[i].start < heap[0]:
                heapq.heappush(heap,arr[i].end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap,arr[i].end)
        return len(heap)
            

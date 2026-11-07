import heapq
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals and newInterval:
            return [newInterval]
        intervals.append(newInterval)
        arr = sorted(intervals, key = lambda x: x[0])
        n = len(arr)
        heap = []
        heapq.heappush(heap,arr[0])
        ans = []
        for i in range(1,n):
            start,end = heapq.heappop(heap)
            if arr[i][0]<=end:
                heapq.heappush(heap,[start,max(arr[i][1],end)])
            else:
                heapq.heappush(heap, [start,end])
                heapq.heappush(heap,arr[i])
                if len(heap) > 1:
                    ans.append(heapq.heappop(heap))
        ans.append(heapq.heappop(heap))
        return ans
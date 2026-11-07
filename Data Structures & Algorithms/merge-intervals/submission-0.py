import heapq
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = sorted(intervals,key = lambda x : x[0])
        heap = []
        n = len(arr)
        heapq.heappush(heap,arr[0])
        ans = []
        for i in range(1,n):
            start,end = heapq.heappop(heap)
            if arr[i][0]<=end:
                heapq.heappush(heap,[start,max(end,arr[i][1])])
            else:
                heapq.heappush(heap,[start,end])
                heapq.heappush(heap,arr[i])
                if len(heap)>1:
                    ans.append(heapq.heappop(heap))
        ans.append(heapq.heappop(heap))
        return ans


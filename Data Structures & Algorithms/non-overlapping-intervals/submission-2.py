class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        arr = sorted(intervals, key = lambda x : x[0])
        n = len(intervals)
        end = arr[0][1]
        count = 0
        for i in range(1,n):
            if arr[i][0] < end:
                count+=1
                end = min(end,arr[i][1])
            else:
                end = arr[i][1]
        return count

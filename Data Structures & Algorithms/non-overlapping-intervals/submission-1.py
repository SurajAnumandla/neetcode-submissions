class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        arr = sorted(intervals, key = lambda x : x[0])
        n = len(intervals)
        ans = [arr[0]]
        count = 0
        for i in range(1,n):
            if arr[i][0] < ans[-1][1]:
                count+=1
                ans[-1][1] = min(ans[-1][1],arr[i][1])
            else:
                ans.append(arr[i])
        return count

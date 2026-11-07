class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = sorted(intervals,key = lambda x : x[0])
        heap = []
        n = len(arr)
        ans = [arr[0]]
        for i in range(1,n):
            if arr[i][0]<=ans[-1][1]:
                ans[-1][1] = max(ans[-1][1],arr[i][1])
            else:
                ans.append(arr[i])
        return ans


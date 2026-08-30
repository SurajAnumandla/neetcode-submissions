class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        start = 0
        end = n-1
        _max = 0
        while start<=end:
            area = min(heights[start],heights[end])*(end-start)
            _max = max(_max,area)
            if heights[start]<heights[end]:
                start+=1
            else:
                end-=1
        return _max
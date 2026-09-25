class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        n = len(heights)
        start = 0
        end = n-1
        while start<end:
            area = max(area,min(heights[start],heights[end]) * (end-start))
            if heights[start]<=heights[end]:
                start+=1
            else:
                end-=1
        return area
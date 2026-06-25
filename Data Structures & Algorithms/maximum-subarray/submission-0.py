class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = float('-inf')
        _sum = 0
        for i in range(len(nums)):
            _sum+=nums[i]
            max_sum = max(max_sum,_sum)

            if _sum < 0:
                _sum = 0
        return max_sum
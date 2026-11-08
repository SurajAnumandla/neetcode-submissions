class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for val in nums:
            res = res^val
        return res
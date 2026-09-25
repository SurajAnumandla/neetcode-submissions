class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = 1
        prefix = [1]*n
        for i in range(0,n):
            prefix[i] = product
            product = product * nums[i]
        product = 1
        for i in range(n-1,-1,-1):
            prefix[i] = prefix[i]*product
            product = product * nums[i]
        return prefix
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [1]*n
        right[0] = 1
        product = 1
        for i in range(1,n):
            product = product*nums[i-1]
            right[i] = product
        
        left = [1]*n
        left[n-1]=1
        product = 1
        for i in range(n-2,-1,-1):
            product = nums[i+1]*product
            left[i] = product
        
        return [right[i]*left[i] for i in range(n)]
        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [1]*n
        product = 1
        for i in range(1,n):
            product = product*nums[i-1]
            right[i] = product
        product = 1
        for i in range(n-2,-1,-1):
            product = product*nums[i+1]
            right[i] = right[i]*product
        return right
        # left = [1]*n
        # product = 1
        # for i in range(n-2,-1,-1):
        #     product = nums[i+1]*product
        #     left[i] = product
        
        # return [right[i]*left[i] for i in range(n)]
        
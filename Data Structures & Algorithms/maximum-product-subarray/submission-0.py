class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = nums[0]
        prev_max = nums[0]
        prev_min = nums[0]
        for i in range(1,len(nums)):
            comb = (nums[i],nums[i]*prev_max,nums[i]*prev_min)
            prev_max = max(comb)
            prev_min = min(comb)
            product = max(product,prev_max)
        return product
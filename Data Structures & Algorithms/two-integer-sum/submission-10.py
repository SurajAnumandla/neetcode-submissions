class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # for i in range(n):
        #     find = target - nums[i]
        #     for j in range(i+1,n):
        #         if nums[j]==find:
        #             return [i,j]
        # return [-1,-1]
        seen = {}
        for i,val in enumerate(nums):
            if target-val in seen:
                return [seen[target-val],i]
            seen[val]= i
        return [-1,-1]
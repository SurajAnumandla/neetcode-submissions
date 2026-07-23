class Solution:
    def max_robber(self,i, nums,dp):
        if i>=len(nums):
            return 0
        
        if dp[i]!=-1:
            return dp[i]

        max_1 = nums[i] + self.max_robber(i+2,nums, dp)
        max_2 = self.max_robber(i+1,nums, dp)
        dp[i] = max(max_1,max_2)
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        return self.max_robber(0,nums,dp)
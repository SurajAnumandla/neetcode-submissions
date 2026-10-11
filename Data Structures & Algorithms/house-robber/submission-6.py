class Solution:
    def dp(self,i,nums,dp):
        if i>=len(nums):
            return 0
        if dp[i]!=-1:
            return dp[i]
        take = nums[i] + self.dp(i+2,nums,dp)
        not_take = self.dp(i+1,nums,dp)
        dp[i] = max(take,not_take)
        return dp[i]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n
        return self.dp(0,nums,dp)
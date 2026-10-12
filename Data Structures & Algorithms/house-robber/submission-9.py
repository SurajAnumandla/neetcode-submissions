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
        if n == 1:
            return nums[0]
        # dp = [-1]*n
        # return self.dp(0,nums,dp)

        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            not_take = dp[i-1]
            take = nums[i] + dp[i-2]
            dp[i] = max(take,not_take)
        return dp[n-1]
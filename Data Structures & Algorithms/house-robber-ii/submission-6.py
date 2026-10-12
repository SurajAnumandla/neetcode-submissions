class Solution:
    def dp(self,i,n,nums,dp):
        if i>=n:
            return 0
        if dp[i]!=-1:
            return dp[i]
        take = nums[i] + self.dp(i+2,n,nums,dp)
        not_take = self.dp(i+1,n,nums,dp)
        dp[i] = max(take,not_take)
        return dp[i]
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        if n==1:
            return nums[0]
        dp_1 = [-1]*n
        dp_2 = [-1]*n

        res_1 = self.dp(0,n-1,nums,dp_1)
        res_2 = self.dp(1,n,nums,dp_2)
        return max(res_1,res_2)
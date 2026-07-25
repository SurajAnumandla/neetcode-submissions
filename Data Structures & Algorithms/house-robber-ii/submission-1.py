class Solution:
    def max_robber(self,i,limit,nums, dp):
        if i>= limit:
            return 0
        if dp[i]!=-1:
            return dp[i]
        # take
        take = nums[i] + self.max_robber(i+2,limit,nums, dp)

        # not take
        not_take = self.max_robber(i+1,limit,nums, dp)
        dp[i] = max(take,not_take) 
        return dp[i]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        dp_1 = [-1]*n
        dp_2 = [-1]*n
        res_1 = self.max_robber(0,n-1,nums,dp_1)
        res_2 = self.max_robber(1,n,nums,dp_2)
        return max(res_1,res_2)
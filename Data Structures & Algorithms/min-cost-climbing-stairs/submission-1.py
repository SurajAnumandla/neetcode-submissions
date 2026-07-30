class Solution:
    def count_steps(self, i,nums, dp):
        if i>=len(nums):
            return 0
        if dp[i]!=-1:
            return dp[i]
        # take
        step_1 = nums[i] + self.count_steps(i+1,nums, dp)
        step_2 = nums[i] + self.count_steps(i+2,nums, dp)
        dp[i] = min(step_1,step_2) 
        return dp[i]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*n 
        res_1 = self.count_steps(0,cost,dp)
        res_2 = self.count_steps(1,cost,dp)
        return min(res_1,res_2)
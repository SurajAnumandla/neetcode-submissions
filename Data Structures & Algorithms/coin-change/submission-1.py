class Solution:
    def count_coints(self, i,nums,amount,_sum, dp):
        if i>=len(nums) and _sum!=amount:
            return float('inf')
        if _sum == amount:
            return 0
        if _sum > amount:
            return float('inf')
        
        if dp[i][_sum]!= -1:
            return dp[i][_sum]
        #take
        take = 1 + self.count_coints(i,nums,amount,_sum+nums[i],dp)
        not_take = self.count_coints(i+1,nums,amount,_sum,dp)
        dp[i][_sum] = min(take,not_take) 
        return dp[i][_sum]
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for j in range(amount+1)] for i in range(n)]
        res = self.count_coints(0,coins,amount,0,dp)
        if res!=float('inf'):
            return res
        return -1
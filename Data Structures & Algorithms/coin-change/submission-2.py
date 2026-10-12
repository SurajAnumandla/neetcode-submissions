class Solution:
    def dp(self,i,total,amount,coins,dp):
        if i>=len(coins) and total!=amount:
            return float('inf')
        if total==amount:
            return 0
        if total>amount:
            return float('inf')
        if dp[i][total]!=-1:
            return dp[i][total]
        take = 1 + self.dp(i,coins[i]+total,amount,coins,dp)
        not_take = self.dp(i+1,total,amount,coins,dp)
        dp[i][total] = min(take,not_take)
        return dp[i][total]
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for j in range(amount+1)]for i in range(len(coins))]
        res = self.dp(0,0,amount,coins,dp)
        if res!=float('inf'):
            return res
        return -1

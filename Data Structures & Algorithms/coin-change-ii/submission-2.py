class Solution:
    def __init__(self):
        self.count = 0
    def count_coins(self,i,nums,amount,_sum,dp):
        if i>=len(nums) and _sum!=amount:
            return 0
        
        if _sum==amount:
            return 1
        if _sum > amount:
            return 0
        
        if dp[i][_sum]!=-1:
            return dp[i][_sum]

        take = self.count_coins(i,nums,amount,_sum+nums[i], dp)
        not_take = self.count_coins(i+1,nums,amount,_sum, dp)

        dp[i][_sum] = take+not_take
        return dp[i][_sum]
    def change(self, amount: int, coins: List[int]) -> int:
        if amount ==0:
            return 1
        n = len(coins)
        dp = [[-1 for j in range(amount+1)]for i in range(n)]
        return self.count_coins(0,coins,amount,0,dp)
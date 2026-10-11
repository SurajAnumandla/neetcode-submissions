class Solution:
    def dp(self,i,n,dp):
        if i==n:
            return 1
        if i>n:
            return 0
        if dp[i]!=0:
            return dp[i]
        climb1 = self.dp(i+1,n,dp)
        climb2 = self.dp(i+2,n,dp)
        dp[i] = climb1+climb2 
        return dp[i]
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        return self.dp(0,n,dp)
class Solution:
    def count_steps(self,i,n, dp):
        if i ==n:
            return 1
        if i>n:
            return 0
        if dp[i]!=0:
            return dp[i]
        #climb 1
        climb_1 = self.count_steps(i+1,n, dp)
        #climb 2
        climb_2 = self.count_steps(i+2,n, dp)
        dp[i] = climb_1 + climb_2 
        return dp[i]
        
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        return self.count_steps(0,n, dp)
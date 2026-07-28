class Solution:
    def sequence(self,i,j,text1,text2,dp):
        if i>=len(text1) or j>=len(text2):
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        ans = 0
        if text1[i]==text2[j]:
            ans = 1 + self.sequence(i+1,j+1,text1,text2,dp)
        else:
            ans = max(self.sequence(i+1,j,text1,text2,dp), self.sequence(i,j+1,text1,text2,dp))
        dp[i][j] = ans
        return ans
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for j in range(len(text2))]for i in range(len(text1))]
        return self.sequence(0,0,text1,text2,dp)
class Solution:
    def find(self,i, prev, nums, dp):
        
        if i >= len(nums):
            return 0
        if dp[i][prev+1] !=-1:
            return dp[i][prev+1]
        #take 
        take = 0
        if prev==-1 or nums[prev] < nums[i]:
            take = 1 + self.find(i+1,i,nums,dp)
        not_take = self.find(i+1,prev,nums,dp)
        dp[i][prev+1] = max(take,not_take)
        return dp[i][prev+1]
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for j in range(n+1)] for i in range(n)]
        return self.find(0,-1,nums, dp)
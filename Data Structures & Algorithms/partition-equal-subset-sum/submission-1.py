class Solution:
    def subset(self, i, nums, total, check_sum,dp):
        if i>= len(nums) and check_sum!=total:
            return False
        if check_sum == total:
            return True
        if check_sum>total:
            return False
        
        if dp[i][check_sum]!=-1:
            return dp[i][check_sum]
        #take
        take = self.subset(i+1,nums,total,check_sum+nums[i], dp)

        not_take = self.subset(i+1,nums,total,check_sum, dp) 
        dp[i][check_sum] = take or not_take
        return dp[i][check_sum]
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1:
            return False
        total = sum(nums)
        if total%2==1:
            return False
        dp = [[-1 for j in range((total//2)+1)] for i in range(n)]
        return self.subset(0,nums,total//2,0, dp)
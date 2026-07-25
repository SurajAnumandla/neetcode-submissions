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
        
        #### Memorization
        
        # n = len(nums)
        # if n==1:
        #     return nums[0]
        # dp_1 = [-1]*n
        # dp_2 = [-1]*n
        # res_1 = self.max_robber(0,n-1,nums,dp_1)
        # res_2 = self.max_robber(1,n,nums,dp_2)
        # return max(res_1,res_2)


        ### Tabulation
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        dp_1 = [0]*n
        dp_1[0] = nums[0]
        dp_1[1] = max(nums[0],nums[1])

        for i in range(2,n-1):
            take = nums[i] + dp_1[i-2]
            not_take = dp_1[i-1]
            dp_1[i] = max(take,not_take)
        
        dp_2 = [0]*n
        dp_2[1] = nums[1]
        dp_2[2] = max(nums[1],nums[2])

        for i in range(3,n):
            take_1 = nums[i] + dp_2[i-2]
            not_take_1 = dp_2[i-1]
            dp_2[i] = max(take_1,not_take_1)
        return max(dp_1[n-2],dp_2[n-1])
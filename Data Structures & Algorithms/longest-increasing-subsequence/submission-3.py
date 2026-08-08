class Solution:
    def lower_bound(self,nums,target):
        n = len(nums)
        l = 0
        r = n -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r = mid-1
            else:
                l=mid+1
        return l
    def find(self, i, prev, nums, dp):
        if i>=len(nums):
            return 0
        
        if dp[i][prev+1]!=-1:
            return dp[i][prev+1]
        #take
        take = 0
        if prev ==-1 or nums[prev]<nums[i]:
            take = 1 + self.find(i+1,i,nums,dp)
        not_take = self.find(i+1,prev,nums,dp)

        dp[i][prev+1] = max(take,not_take)
        return dp[i][prev+1] 
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [[-1 for j in range(n+1)] for i in range(n)]
        # return self.find(0,-1,nums,dp)

        lis = []
        n = len(nums)
        lis.append(nums[0])

        for i in range(1,n):
            if nums[i]>lis[-1]:
                lis.append(nums[i])
            else:
                lb = self.lower_bound(lis,nums[i])
                lis[lb] = nums[i]
        return len(lis)

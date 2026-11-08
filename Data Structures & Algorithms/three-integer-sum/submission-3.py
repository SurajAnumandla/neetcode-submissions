class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            start = i+1
            end = n-1
            while start<end:
                _sum = nums[i] + nums[start] + nums[end]
                if _sum < 0:
                    start+=1
                elif _sum > 0:
                    end-=1
                else:
                    res.append([nums[i],nums[start],nums[end]])

                    while start<end and nums[start]==nums[start+1]:
                        start+=1
                    while start<end and nums[end]==nums[end-1]:
                        end-=1
                    start+=1
                    end-=1
        return res                    
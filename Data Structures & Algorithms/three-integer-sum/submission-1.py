class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue 
            target = nums[i]
            start = i + 1
            end = n - 1
            while start<end:
                _sum = nums[start] + nums[end]
                if _sum + target < 0:
                    start+=1
                elif _sum + target > 0:
                    end-=1
                else:
                    result.append([nums[i],nums[start],nums[end]])
                    while start<end and nums[start] == nums[start+1]:
                        start+=1
                    while start<end and nums[end] == nums[end-1]:
                        end-=1
                    start+=1
                    end-=1
        return result
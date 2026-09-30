class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_length = 0
        for num in seen:
            if num-1 not in seen:
                temp = num
                length = 1
                while temp+1 in seen:
                    temp+=1
                    length+=1
                max_length = max(max_length,length)
        return max_length
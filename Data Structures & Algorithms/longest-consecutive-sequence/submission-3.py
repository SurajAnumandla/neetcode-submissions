class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)
        for val in nums:
            if val-1 not in seen:
                length = 1
                curr = val
                while curr+1 in seen:
                    curr+=1
                    length+=1
                longest = max(longest,length)
        return longest
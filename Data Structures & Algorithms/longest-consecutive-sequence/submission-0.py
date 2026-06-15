class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in nums:
            length = 1
            curr = num
            while curr+1 in seen:
                curr+=1
                length+=1
            longest = max(longest,length)
        return longest
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic  = {}
        start = 0
        max_size = 0

        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= start:
                start = dic[s[i]]+1
            dic[s[i]] = i
            max_size = max(max_size,i-start+1)
        return max_size
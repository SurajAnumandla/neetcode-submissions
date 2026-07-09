class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = {}
        max_window = 0
        max_freq = 0
        left = 0
        for right in range(n):
            freq[s[right]] = freq.get(s[right],0)+1
            max_freq = max(max_freq,freq[s[right]])

            while (right-left+1) - max_freq > k:
                freq[s[left]]-=1
                left+=1
            max_window = max(max_window,right-left+1)
        return max_window
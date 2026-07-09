class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if n < m:
            return False
        freq = {}
        for c in s1:
            freq[c] = freq.get(c,0)+1
        
        seen = {}
        for i in range(m):
            seen[s2[i]] = seen.get(s2[i],0)+1
        
        if seen == freq:
            return True
        
        left = 0
        for i in range(m,n):
            seen[s2[left]] = seen.get(s2[left])-1
            if seen[s2[left]] == 0:
                del seen[s2[left]]
            left+=1
            seen[s2[i]] = seen.get(s2[i],0)+1
            if seen == freq:
                return True
        return False

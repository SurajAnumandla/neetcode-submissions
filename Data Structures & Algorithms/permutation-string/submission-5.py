from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n=len(s2)
        if m>n:
            return False

        freq1 = Counter(s1)
        freq2 = Counter(s2[:m])

        if freq1==freq2:
            return True
        
        for i in range(m,n):
            freq2[s2[i]]+=1
            freq2[s2[i-m]]-=1
            if freq2[s2[i-m]] == 0:
                del freq2[s2[i-m]]
            if freq1==freq2:
                return True
        # for i in range(n-m+1):
        #     if Counter(s2[i:m+i])==freq:
        #         return True
        return False
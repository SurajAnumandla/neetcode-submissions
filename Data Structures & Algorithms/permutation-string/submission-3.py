from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n=len(s2)
        freq = Counter(s1)
        for i in range(0,n):
            if Counter(s2[i:m+i])==freq:
                return True
        return False
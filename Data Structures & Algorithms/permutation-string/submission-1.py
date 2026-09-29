from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        freq = Counter(s1)
        n = len(s2)
        for i in range(n-m+1):
            if Counter(s2[i:m+i])== freq:
                return True
        return False
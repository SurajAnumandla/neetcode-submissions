class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res1 = {}
        res2 = {}

        for c in s:
            res1[c] = res1.get(c,0)+1
        
        for c in t:
            res2[c] = res2.get(c,0)+1
        
        return res1==res2
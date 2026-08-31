class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq  = [0]*26
        for c1,c2 in zip(s,t):
            freq[ord(c1)-ord('a')]+=1
            freq[ord(c2)-ord('a')]-=1
        for v in freq:
            if v!=0:
                return False
        return True
        # res1 = {}
        # res2 = {}

        # for c in s:
        #     res1[c] = res1.get(c,0)+1
        
        # for c in t:
        #     res2[c] = res2.get(c,0)+1
        
        # return res1==res2
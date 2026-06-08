class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq = [0]*26
        for c in zip(s,t):
            c1 = c[0]
            c2 = c[1]
            freq[ord(c1)-ord('a')] +=1
            freq[ord(c2)-ord('a')] -=1
        
        for v in freq:
            if v!=0:
                return False
        return True
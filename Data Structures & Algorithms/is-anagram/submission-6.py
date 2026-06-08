class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        # return sorted(s) == sorted(t)


        # Freq dict method 1
        # if len(s)!= len(t):
        #     return False

        # freq = dict()
        # for c in s:
        #     freq[c] = freq.get(c,0) + 1
        
        # for c in t:
        #     freq[c] = freq.get(c,0)-1
        
        # for k,v in freq.items():
        #     if v!=0:
        #         return False
        # return True

        # Freq dict method 2
        if len(s)!= len(t):
            return False

        freq = dict()
        for c in range(len(s)):
            
            c1 = s[c]
            c2 = t[c]
            
            freq[c1] = freq.get(c1,0) + 1
            freq[c2] = freq.get(c2,0) - 1

        for v in freq.values():
            if v!=0:
                return False
        return True



        #Freq array method

        # f = [0]*26

        # if len(s)!= len(t):
        #     return False

        # for i in range(len(s)):
        #     f[ord(s[i]) - ord('a')] += 1
        #     f[ord(t[i])-ord('a')]-=1

        # for val in f:
        #     if val!=0:
        #         return False
        # return True
        
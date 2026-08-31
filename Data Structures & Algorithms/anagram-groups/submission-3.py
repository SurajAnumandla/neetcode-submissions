from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for s in strs:
            freq = [0]*26
            for c in s:
                freq[ord(c)-ord('a')]+=1
            seen[tuple(freq)].append(s)
        res = []
        for val in seen.values():
            res.append(val)
        return res


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            freq = [0]*26
            for c in s:
                freq[ord(c)-ord('a')]+=1
            key = tuple(freq)
            res[key].append(s)
        
        return list(res.values())

        # res = {} 

        # for s in strs:
        #     key = ''.join(sorted(s))

        #     if key not in dic:
        #         dic[key] = [s]
        #     else:
        #         dic[key].append(s)

        # return list(dic.values())
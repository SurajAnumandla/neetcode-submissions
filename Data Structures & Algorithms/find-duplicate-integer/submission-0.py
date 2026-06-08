class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = {}
        for v in nums:
            res[v] = res.get(v,0)+1
        
        for key,val in res.items():
            if val > 1:
                return key
        
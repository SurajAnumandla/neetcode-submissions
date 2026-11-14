class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        while n:
            res[n] = bin(n).count('1')
            n = n-1
        return res
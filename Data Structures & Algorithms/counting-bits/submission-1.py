class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        # while n:
        #     res[n] = bin(n).count('1')
        #     n = n-1
        # return res

        for i in range(1,n+1):
            res[i] = res[i>>1] + (i&1)
        return res
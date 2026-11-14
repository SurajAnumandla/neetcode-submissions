from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        freq = Counter(str(bin(n))) 
        return freq.get("1",0)
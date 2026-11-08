from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        freq = Counter(list(bin(n)))
        return freq["1"]
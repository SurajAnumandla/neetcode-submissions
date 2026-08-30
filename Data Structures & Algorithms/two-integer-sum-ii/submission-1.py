class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        start = 0
        end = n-1
        while start<end:
            _sum = numbers[start] + numbers[end]
            if  _sum < target:
                start+=1
            elif _sum > target:
                end-=1
            else:
                return [start+1,end+1]
        return [-1,-1]
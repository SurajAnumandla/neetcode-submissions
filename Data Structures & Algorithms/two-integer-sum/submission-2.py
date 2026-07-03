class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            reqd = target-nums[i]

            if reqd in seen:
                return [seen.get(reqd),i]
            seen[nums[i]] = i
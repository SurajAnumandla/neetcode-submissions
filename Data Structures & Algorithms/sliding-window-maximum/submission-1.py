class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)
        res = []
        q.append(0)
        for i in range(1,k):
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)
        for i in range(k,n):
            res.append(q[0])
            idx = i-k
            if idx in q:
                q.popleft()
            while q and nums[i]>nums[q[-1]]:
                q.pop()
            q.append(i)
        res.append(q[0])
        return [nums[i] for i in res]
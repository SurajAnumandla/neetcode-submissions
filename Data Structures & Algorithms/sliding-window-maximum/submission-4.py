class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)
        res = []
        for i in range(k):
            while q and nums[i]>q[-1]:
                q.pop()
            q.append(nums[i])
        
        for i in range(k,n):
            res.append(q[0])
            if nums[i-k] == q[0]:
                q.popleft()
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
        res.append(q[0])
        return res

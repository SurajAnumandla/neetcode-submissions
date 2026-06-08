class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0]* n

        right = 1
        for i in range(n):
            arr[i] = right
            right = right * nums[i]
        
        # brr = [0]*n
        left = 1
        for i in range(n-1,-1,-1):
            arr[i] = arr[i]*left
            left = left * nums[i]

        return arr
        
        # res = [0]*n 
        # for i in range(n):
        #     res[i] = arr[i]*brr[i]

        # return res
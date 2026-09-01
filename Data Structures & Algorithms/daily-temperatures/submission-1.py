class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        st = []
        for i in range(n-1,-1,-1):
            while st and nums[i]>=st[-1][0]:
                    st.pop()
            if st:
                res[i] = st[-1][1]-i
            st.append((nums[i],i))
        return res

        # for i in range(n):
        #     count = 1
        #     for j in range(i+1,n):
        #         if nums[j] > nums[i]:
        #             res[i] = count
        #             break
        #         count+=1
        # return res
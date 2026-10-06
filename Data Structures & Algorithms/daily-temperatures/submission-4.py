class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        n = len(temperatures)
        res = [0]*n

        for i in range(n-1,-1,-1):
            while st and temperatures[i] >= temperatures[st[-1]]:
                st.pop()
            if st:
                res[i] = st[-1] - i
            st.append(i)
        return res
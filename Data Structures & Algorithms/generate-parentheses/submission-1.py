class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        st = []
        def dfs(_open,_close):
            if _open == _close == n:
                res.append("".join(st))
                return
            if _open<n:
                st.append('(')
                dfs(_open+1,_close)
                st.pop()
            if _close<_open:
                st.append(')')
                dfs(_open,_close+1)
                st.pop()
        dfs(0,0)
        return res
                

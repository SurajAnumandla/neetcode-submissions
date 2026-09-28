class Solution:
    def isValid(self, s: str) -> bool:
        seen = {"]":"[","}":"{",")":"("}
        st = []
        for c in s:
            if st and c in seen:
                val = st.pop()
                if val!=seen.get(c):
                    return False
            else:
                st.append(c)
        return len(st)==0
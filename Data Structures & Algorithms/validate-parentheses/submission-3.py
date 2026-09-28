class Solution:
    def isValid(self, s: str) -> bool:
        seen = {"]":"[","}":"{",")":"("}
        st = []
        for c in s:
            if c in seen:
                if not st or st.pop()!=seen.get(c):
                    return False
            else:
                st.append(c)
        return len(st)==0
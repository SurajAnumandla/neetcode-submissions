class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for val in tokens:
            if val not in {"+","*","-","/"}:
                st.append(val)
            else:
                a = int(st.pop())
                b = int(st.pop())
                if val == "+":
                    st.append(a+b)
                elif val=="*":
                    st.append(a*b)
                elif val=="-":
                    st.append(b-a)
                else:
                    st.append(int(b/a))
        return int(st[-1])
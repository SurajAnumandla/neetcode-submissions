class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])

        st = []
        ans = None
        for val in tokens:
            if val!="+" and val!="*" and val!="-" and val!="/":
                st.append(val)
            else:
                if val == "+":
                    ans = 0
                    ans+=int(st.pop())
                    ans+=int(st.pop())
                elif val=="*":
                    ans = 1
                    ans*=int(st.pop())
                    ans*=int(st.pop())
                elif val=="-":
                    val1 = int(st.pop())
                    val2 = int(st.pop())
                    ans = val2-val1
                else:
                    val1 = int(st.pop())
                    val2 = int(st.pop())
                    ans = int(val2/val1)
                st.append(int(ans))
        return ans
class MinStack:

    def __init__(self):
        self.st = []
        self.min = float('inf')        

    def push(self, val: int) -> None:
        self.min = min(self.min,val)
        self.st.append((val,self.min))

    def pop(self) -> None:
        val = self.st.pop()
        if self.st:
            self.min = self.st[-1][1]
        else:
            self.min = float('inf')
        return val[0]
    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]

class MinStack:

    def __init__(self):  
        self.st = []
        self._min = float('inf')

    def push(self, val: int) -> None:
        self._min = min(self._min,val)
        self.st.append((val,self._min))
    
    def pop(self) -> None:
        val = self.st.pop()[0]
        if self.st:
            self._min = self.st[-1][1] 
        else:
            self._min = float('inf')
        return val
    def top(self) -> int:
        return self.st[-1][0]
    def getMin(self) -> int:
        return self.st[-1][1]
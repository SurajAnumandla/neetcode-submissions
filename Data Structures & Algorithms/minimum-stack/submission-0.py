class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        curr_min = min(self.st[-1][1],val) if self.st else val
        self.st.append((val,curr_min))
    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]

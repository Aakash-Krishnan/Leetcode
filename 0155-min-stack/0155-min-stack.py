class MinStack:

    def __init__(self):
        self.stack = []
        self.Min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.Min:
            self.Min.append(val)
        else:
            if self.Min[-1] >= val:
                self.Min.append(val)


    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.Min[-1]:
            self.Min.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.Min:
            return self.Min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
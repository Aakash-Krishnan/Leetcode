class MyQueue:

    def __init__(self):
        self.stack = []
        self.stackq = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pour(self):
        while self.stack:
            self.stackq.append(self.stack.pop())
        
    def pop(self) -> int:
        if not self.stackq:
            self.pour()
        return self.stackq.pop()
    
    def peek(self) -> int:
        if not self.stackq:
            self.pour()
        return self.stackq[-1]
        

    def empty(self) -> bool:
        return not self.stackq and not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
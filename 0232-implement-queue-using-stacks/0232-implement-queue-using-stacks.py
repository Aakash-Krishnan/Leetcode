class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def fill(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
    def pop(self) -> int:
        if not self.stack2:
            self.fill()
            
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            self.fill()
            
        return self.stack2[-1]

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
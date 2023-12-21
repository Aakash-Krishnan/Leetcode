class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.curr.next = newNode
        newNode.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr and self.curr.prev and steps > 0:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr and self.curr.next and steps > 0:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
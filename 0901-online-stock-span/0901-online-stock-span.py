class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        val = 1
        while self.stack and self.stack[-1][0] <= price:
            oldPrice, oldVal = self.stack.pop()
            val += oldVal
        
        self.stack.append([price, val])
        return val


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
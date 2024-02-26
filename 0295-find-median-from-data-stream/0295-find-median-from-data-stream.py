class MedianFinder:

    def __init__(self):
        self.maxHq = []
        self.minHq = []

    def addNum(self, num: int) -> None:
        if not self.minHq:
            heappush(self.minHq, -1 * num)
        else:
            if num > -(self.minHq[0]):
                heappush(self.maxHq, num)
            else:
                heappush(self.minHq, -1 * num)
        
        if abs(len(self.minHq) - len(self.maxHq)) > 1:
            if len(self.minHq) > len(self.maxHq):
                heappush(self.maxHq, -1 * (heappop(self.minHq)))
            else:
                heappush(self.minHq, -1 * (heappop(self.maxHq)))
                
    def findMedian(self) -> float:
        if len(self.minHq) > len(self.maxHq):
            return (-1 * self.minHq[0])
        elif len(self.minHq) < len(self.maxHq):
            return self.maxHq[0]

        return (-1 * self.minHq[0] + self.maxHq[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
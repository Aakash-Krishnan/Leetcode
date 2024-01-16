class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            idx = self.map[val]
            lastVal = self.list[-1]
            self.list[idx] = lastVal
            self.list.pop()
            self.map[lastVal] = idx
            self.map.pop(val)
           
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
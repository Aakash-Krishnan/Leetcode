class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        fmap = Counter(nums)
        res = set()
        minHq = []
        for key, val in fmap.items(): 
            if len(minHq) < k:
                heappush(minHq, (val, key))
                res.add(key)
            else:
                if minHq[0][0] < val:
                    res.remove(heappop(minHq)[1])
                    heappush(minHq, (val, key))
                    res.add(key)
        return list(res)
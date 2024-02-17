class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        fmap = {}
        for i in time:
            val = i % 60
            p = 0
            if val:
                p = 60 - val
            
            if p in fmap:
                res += fmap[p]
            
            fmap[val] = fmap.get(val, 0) + 1
        
        return res
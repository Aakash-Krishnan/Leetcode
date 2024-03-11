class Solution:
    def customSortString(self, order: str, s: str) -> str:
        fmap = {}
        for c in s:
            fmap[c] = fmap.get(c, 0) + 1
        
        res = ''
        for c in order:
            if c in fmap:
                res += (c * fmap[c])
                fmap.pop(c)
        
        for key, val in fmap.items():
            res += (key * val)
        
        return res
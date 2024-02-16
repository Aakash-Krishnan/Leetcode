class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        fmap = {}
        for i in arr:
            fmap[i] = fmap.get(i, 0) + 1
        
        cnt = len(fmap)
        for i in sorted(fmap.values()):
            while k and i:
                k -= 1
                i -= 1
            if not i:
                cnt -= 1
            if not k: break
        
        return cnt
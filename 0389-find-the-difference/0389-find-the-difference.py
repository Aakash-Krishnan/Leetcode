class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        fmap = {}
        
        for i in s:
            if i in fmap:
                fmap[i] += 1
            else:
                fmap[i] = 1
            
        for i in t:
            if i in fmap:
                if fmap[i] > 0:
                    fmap[i] -= 1
                if fmap[i] == 0:
                    fmap.pop(i)
            else:
                return i
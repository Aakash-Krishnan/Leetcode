class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        fmap = {}
        
        for i in words:
            for j in i:
                if j in fmap:
                    fmap[j] += 1
                else:
                    fmap[j] = 1
        
        for i in fmap:
            if fmap[i] % len(words) != 0:
                return False
        
        return True
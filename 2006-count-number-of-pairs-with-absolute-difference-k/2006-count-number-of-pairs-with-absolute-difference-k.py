class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        fmap = {}
        
        for i in nums:
            try:
                fmap[i] += 1
            except KeyError:
                fmap[i] = 1
        
        cnt = 0
        for i in fmap:
            val = k + i
            if val  == i and fmap[val] > 1:
                cnt += fmap[val] * fmap[i]
            elif val != i and val in fmap:
                cnt += fmap[val] * fmap[i]
        return cnt
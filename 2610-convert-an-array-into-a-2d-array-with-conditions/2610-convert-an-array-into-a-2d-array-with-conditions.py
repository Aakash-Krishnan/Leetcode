class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        fmap = {}
        for i in nums:
            fmap[i] =  fmap.get(i, 0) + 1
        
        ans = []
        while fmap:
            sub = []
            delet = []
            for id, val in fmap.items():
                sub.append(id)
                val -= 1
                if not val:
                    delet.append(id)
                fmap[id] = val
            ans.append(sub)
            for i in delet:
                del fmap[i]
                
        return ans
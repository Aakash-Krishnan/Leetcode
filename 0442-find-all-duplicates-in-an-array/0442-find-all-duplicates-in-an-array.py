class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        fset = set()
        ans = []
        for i in nums:
            if i in fset:
                ans.append(i)
                fset.remove(i)
            else:
                fset.add(i)
        
        return ans
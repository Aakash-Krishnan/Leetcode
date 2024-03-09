class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        fset = set(nums1)
        for i in nums2:
            if i in fset:
                return i
        
        return -1
        
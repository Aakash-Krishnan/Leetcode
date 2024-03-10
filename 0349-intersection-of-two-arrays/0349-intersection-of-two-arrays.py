class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        fset = set(nums1)
        res = set()
        for i in nums2:
            if i in fset:
                res.add(i)
        
        return list(res)
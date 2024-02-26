class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        lo, hi = 0, len(nums) - 1 
        largest = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[-1]:
                largest = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return nums[largest + 1]
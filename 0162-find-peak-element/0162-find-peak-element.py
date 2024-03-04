class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        
        lo = 1
        hi = len(nums)-2
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] < nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        # if nums[0] < nums[1]:
        #     return 1
        # if nums[-1] < nums[-2]:
        #     return len(nums)-2
        
        return -1
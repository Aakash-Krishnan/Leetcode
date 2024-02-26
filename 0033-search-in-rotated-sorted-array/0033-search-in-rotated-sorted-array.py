class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(lo, hi):
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1
        
        if nums[0] <= nums[-1]:
            return binarySearch(0, len(nums) - 1)
        
        largest = -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[-1]:
                largest = mid 
                lo = mid + 1
            else:
                hi = mid - 1
        
        if nums[-1] >= target:
            return binarySearch(largest + 1, len(nums) - 1)
        else:
            return binarySearch(0, largest)
    
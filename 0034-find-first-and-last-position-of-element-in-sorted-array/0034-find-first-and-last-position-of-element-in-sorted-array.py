class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        N = len(nums)
        hi = N-1
        ans = [-1, -1]
        idx, flag = 0, False
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                ans[0] = mid
                hi = mid - 1
                if not flag:
                    flag = True
                    idx = mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        lo = idx
        hi = N - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                ans[1] = mid
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return ans
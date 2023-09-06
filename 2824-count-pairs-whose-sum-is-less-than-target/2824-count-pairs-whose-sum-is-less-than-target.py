class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        cnt = 0
        lo , hi = 0, len(nums) - 1
        while lo < hi:
            if nums[lo] + nums[hi] < target:
                cnt += hi - lo
                lo += 1
            else:
                hi -= 1
        return cnt
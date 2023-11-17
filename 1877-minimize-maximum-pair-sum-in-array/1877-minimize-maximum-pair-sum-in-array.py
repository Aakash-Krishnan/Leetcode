class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        L = 0
        R = len(nums)-1
        ans = 0
        while L < R:
            ans = max(ans, nums[L]+nums[R])
            L += 1
            R -= 1
        return ans
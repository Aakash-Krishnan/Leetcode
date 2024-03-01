class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            h1, h2 = 0, 0
            for i in range(len(nums)):
                temp = max(h1 + nums[i], h2)
                h1 = h2
                h2 = temp
            return h2
        
        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))
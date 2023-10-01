class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(len(nums)):
            if nums[i] < 1:
                nums[i] = N + 1
        
        for i in range(len(nums)):
            x = abs(nums[i])
            if x <= N:
                nums[x-1] = -abs(nums[x-1])
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        return N+1
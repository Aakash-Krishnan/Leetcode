class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        n = len(nums)
        for i in range(len(nums)):
            if not i:
                Sl = 0
            else:
                Sl = nums[i-1]
            
            Sr = nums[n-1] - nums[i]
            if Sl == Sr:
                return i
        
        return -1
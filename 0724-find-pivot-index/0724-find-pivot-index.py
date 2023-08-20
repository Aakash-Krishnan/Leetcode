class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        
        N = len(nums)
        for i in range(len(nums)):
            if i == 0:
                Sl = 0
            else:
                Sl = nums[i-1]
            Sr = nums[N - 1] - nums[i]
            
            if Sl == Sr:
                return i
        else:
            return -1
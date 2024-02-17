class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = abs(nums[i])-1
            if nums[x] < 0:
                return x+1
            nums[x] = -abs(nums[x])
        

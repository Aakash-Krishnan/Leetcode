class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                nums.append(0)
                nums.remove(0)
            j += 1
        print(nums)
        
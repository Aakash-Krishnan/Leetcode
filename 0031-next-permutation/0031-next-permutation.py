class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 3:
            return nums.reverse()
        
        pivot = -1
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        
        if pivot == -1:
            return nums.reverse()
        
        for i in range(len(nums)-1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                break
        
        L = pivot + 1
        R = len(nums) - 1
        
        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1
        
        return nums
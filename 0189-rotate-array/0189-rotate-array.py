class Solution:
    
    def rotateCode(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if len(nums) < 2:
            return nums
        j = len(nums) -1
        self.rotateCode(nums, 0, j)
        j = k-1
        self.rotateCode(nums, 0, j)
        j = len(nums) -1
        self.rotateCode(nums, k, j)
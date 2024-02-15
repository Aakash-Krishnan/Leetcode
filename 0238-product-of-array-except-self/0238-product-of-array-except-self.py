class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        res[0] = nums[0]
        for i in range(1, n):
            res[i] = res[i-1] * nums[i]
        
        
        for i in range(n-1, -1, -1):
            if i == n-1:
                val = nums[-1]
                nums[i] = res[i-1]
            elif i == 0:
                nums[i] = val
            else:
                mul = nums[i]
                nums[i] = res[i-1] * val
                val *= mul
        
        return nums
            
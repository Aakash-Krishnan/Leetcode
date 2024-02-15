class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = -1
        Sum = nums[0] + nums[1]
        
        for i in range(2, len(nums)):
            if Sum > nums[i]:
                Sum += nums[i]
                ans = max(ans, Sum)
            else:
                Sum += nums[i]
        return ans
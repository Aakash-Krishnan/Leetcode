class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # nums.sort()
        # return (nums[-1] * nums[-2]) - (nums[0] * nums[1])
        firstBig = secondBig = 0
        firstSmall = secondSmall = float('inf')
        
        for i in nums:
            if i < firstSmall:
                firstSmall, secondSmall = i, firstSmall
            elif i < secondSmall:
                secondSmall = i
            
            if i > firstBig:
                firstBig, secondBig = i, firstBig
            elif i > secondBig:
                secondBig = i
            
        return (firstBig * secondBig) - (firstSmall * secondSmall)
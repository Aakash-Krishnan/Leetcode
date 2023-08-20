class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        
        arr = []
        for i in range(len(nums)):
            if i == 0:
                Sum = nums[len(nums)-1] - nums[i]
                arr.append(Sum)
            elif i == len(nums)-1:
                arr.append(nums[i-1])
            else:
                Sl = nums[i-1]
                Sr = nums[len(nums)-1] - nums[i]
                Sum = abs(Sl - Sr)
                arr.append(Sum)
        return arr
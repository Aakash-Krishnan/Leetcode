class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fmap = {}
        
        for i in range(len(nums)):
            val = target - nums[i]
            if val in fmap:
                return [i, fmap[val]]
            fmap[nums[i]] = i
        
        
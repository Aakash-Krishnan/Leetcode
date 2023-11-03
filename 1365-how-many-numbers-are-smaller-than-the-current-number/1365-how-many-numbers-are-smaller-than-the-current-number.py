class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        temp = sorted(nums)
        fmap= {}
        for i in range(len(temp)):
            if temp[i] not in fmap:
                fmap[temp[i]] = i
        
        for i in range(len(nums)):
            arr.append(fmap[nums[i]])
        return arr
        
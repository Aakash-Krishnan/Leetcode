class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = -102
        k = 0
        L, R = 0, 0
        while R < len(nums):
            if prev != nums[R]:
                k += 1
                prev = nums[R]
                nums[L] = nums[R]
                L += 1
            R += 1
        return k
        
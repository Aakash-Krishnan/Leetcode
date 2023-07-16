class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag = False
        for i, value in enumerate(nums):
            x = target - value
            for j, innerValue in enumerate(nums):
                if i != j:
                    if x == innerValue:
                        flag = True
                        return [i , j]
            if flag:
                break



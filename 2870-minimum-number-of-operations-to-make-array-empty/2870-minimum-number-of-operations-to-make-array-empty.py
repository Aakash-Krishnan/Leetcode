from collections import Counter
import math
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        fmap = Counter(nums)
        ans = 0
        for i in fmap.values():
            if i < 2:
                return -1
            ans += math.ceil(i / 3)
        return ans
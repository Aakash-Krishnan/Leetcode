class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        pos = 0
        while left != right:
            left = left >> 1 
            right = right >> 1
            pos += 1
        return right << pos
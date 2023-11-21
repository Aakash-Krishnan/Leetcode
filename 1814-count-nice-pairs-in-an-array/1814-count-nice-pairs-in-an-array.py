def reverse(A):
    Sum = 0
    while A > 0:
        Sum = Sum * 10 + A % 10
        A //= 10
    return Sum

class Solution:
    def countNicePairs(self, nums):
        fmap = {}
        cnt = 0
        mod= (10**9)+7
        for i in nums:
            Sum = i - reverse(i)
            if Sum in fmap:
                cnt = (cnt + fmap[Sum]) % mod
                fmap[Sum] += 1
            else:
                fmap[Sum] = 1
        return cnt
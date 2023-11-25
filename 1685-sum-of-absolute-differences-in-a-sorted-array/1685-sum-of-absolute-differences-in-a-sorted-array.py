class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        arr = []
        ps = [nums[0]]
        ss = [nums[-1]]
        for i in range(1,n):
            ps.append(nums[i] + ps[i-1])
        
        for i in range(n-2, -1, -1):
            ss.insert(0, nums[i] + ss[0])
        
        for i in range(n):
            val = ((nums[i] * i) - ps[i]) + (ss[i] - (nums[i] * (n - i - 1)))
            arr.append(val)
        return arr

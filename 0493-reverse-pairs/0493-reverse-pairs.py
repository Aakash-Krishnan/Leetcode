class Solution:
    cnt = 0
    def merge(self, left, right):
        n, m = len(left), len(right)
        i, j = 0, 0
        while i < n and j < m:
            if left[i] > 2* right[j]:
                Solution.cnt += n - i
                j += 1
            else:
                i += 1
        
        return sorted(left+right)
    
    def mergeSort(self, nums):
        N = len(nums)
        if N == 1:
            return nums
        mid = N//2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left, right)
        
        
    def reversePairs(self, nums):
        self.mergeSort(nums)
        val = Solution.cnt
        Solution.cnt = 0
        return val
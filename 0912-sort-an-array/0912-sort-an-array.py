class Solution:
    def merge(self, left, right):
        n, m = len(left), len(right)
        i, j = 0, 0
        ans = []
        while i < n and j < m:
            if left[i] > right[j]:
                ans.append(right[j])
                j += 1
            else:
                ans.append(left[i])
                i += 1
        while i < n:
            ans.append(left[i])
            i += 1
        while j < m:
            ans.append(right[j])
            j += 1
        return ans

    def mergeSort(self, A):
        if len(A) == 1:
            return A

        mid = len(A)//2
        left = self.mergeSort(A[:mid])    
        right = self.mergeSort(A[mid:])    
        return self.merge(left, right)
    
    
    
    def sortArray(self, nums: List[int]) -> List[int]:
        ans = self.mergeSort(nums)
        return ans 
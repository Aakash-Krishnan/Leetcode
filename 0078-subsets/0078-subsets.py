
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        def subArray(A, idx):
            # global ans, arr
            if idx == len(A):
                ans.append(arr[:])
                return 

            subArray(A, idx+1)
            arr.append(A[idx])
            subArray(A, idx+1)
            arr.pop()


        subArray(nums, 0)
        return ans
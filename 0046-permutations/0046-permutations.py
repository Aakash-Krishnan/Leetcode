class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutations(A, pos, ans):
            if pos == len(A):
                ans.append(A[:])
                return 
            
            for i in range(pos, len(A)):
                A[i], A[pos] = A[pos], A[i]
                permutations(A, pos+1, ans)
                A[i], A[pos] = A[pos], A[i]
                
        ans = []
        permutations(nums, 0, ans)
        return ans
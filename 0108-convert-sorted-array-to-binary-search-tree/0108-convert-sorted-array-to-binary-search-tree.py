# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(lo, hi):
            if lo > hi:
                return None
            mid = lo + (hi - lo) // 2
            node = TreeNode(nums[mid])
            node.left = dfs(lo, mid-1)
            node.right = dfs(mid+1, hi)
            return node
        
        return dfs(0, len(nums)-1)
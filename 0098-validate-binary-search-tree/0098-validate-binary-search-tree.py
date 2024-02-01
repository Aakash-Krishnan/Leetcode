# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, Min, Max):
            if not root:
                return True
            if not (Min <= root.val <= Max):
                return False
            return dfs(root.left, Min, root.val - 1) and dfs(root.right, root.val + 1, Max)
            
        
        return dfs(root, float("-inf"), float("inf"))
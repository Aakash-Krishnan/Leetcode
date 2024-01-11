# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, Min, Max):
            if not node:
                return Max - Min
            
            Min = min(Min, node.val)
            Max = max(Max, node.val)
            
            left = dfs(node.left, Min, Max)
            right = dfs(node.right, Min, Max)
            
            return max(left, right)
        
        return dfs(root, root.val, root.val)
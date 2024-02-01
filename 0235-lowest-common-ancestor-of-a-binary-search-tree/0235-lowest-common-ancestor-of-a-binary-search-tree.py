# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, Min, Max):
            if Min < Max < root.val:
                return dfs(root.left, Min, Max)
            elif root.val < Min < Max:
                return dfs(root.right, Min, Max)
            return root
        
        
        Min, Max = min(p.val, q.val), max(p.val, q.val)
        return dfs(root, Min, Max)
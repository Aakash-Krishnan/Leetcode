# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        def dfs(root, take=True):
            if not root:
                return 0
            if (root, take) in cache:
                return cache[(root, take)]
            
            res = (dfs(root.left, True) + dfs(root.right, True))
            
            if take:
                res = max(res, root.val + (dfs(root.left, False) + dfs(root.right, False)))
                
            cache[(root, take)] = res
            return res
        
        return dfs(root)
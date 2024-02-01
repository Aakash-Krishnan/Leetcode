# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        k = root.val
        
        def dfs(root, k):
            nonlocal res
            if not root:
                return 
            if root.val >= k:
                res += 1
                k = root.val
            dfs(root.left, k)
            dfs(root.right, k)
            
        
        dfs(root, root.val)
        return res
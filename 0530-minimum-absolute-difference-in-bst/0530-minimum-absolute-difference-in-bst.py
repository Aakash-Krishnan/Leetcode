# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float('inf')
        prev = None
        def dfs(root):
            nonlocal prev, res
            if not root:
                return False
            
            dfs(root.left)
            if prev!= None:
                res = min(res, root.val - prev)
            prev = root.val
            dfs(root.right)
        
        dfs(root)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def maxSum(root):
            nonlocal res
            if not root:
                return 0
            left = max(maxSum(root.left), 0)
            right = max(maxSum(root.right), 0)
            
            res = max(res, root.val + left + right)
            return root.val + max(left, right)
        
        maxSum(root)
        return res
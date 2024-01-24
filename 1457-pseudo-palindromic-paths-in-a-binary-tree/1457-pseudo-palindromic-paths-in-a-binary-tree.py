# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        cache = defaultdict(int)
        odd = 0
        
        def dfs(root):
            nonlocal odd
            if not root:
                return 0
            
            cache[root.val] += 1
            changeOdd = 1 if cache[root.val] % 2 else -1
            odd += changeOdd
            
            if not root.left and not root.right:
                res = 1 if odd < 2 else 0
            else:
                res = dfs(root.left) + dfs(root.right)
            
            odd -= changeOdd
            cache[root.val] -= 1
            return res
        
        return dfs(root)
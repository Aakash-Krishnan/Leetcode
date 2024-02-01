# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, A: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        res = []

        def check(node):
            nonlocal prev
            if prev and prev.val > node.val:
                res.append(prev)
                res.append(node)
            prev = A


        while A:
            if not A.left:
                check(A)
                A = A.right
            else:
                temp = A.left
                while temp.right and temp.right != A:
                    temp = temp.right
                
                if not temp.right:
                    temp.right = A
                    A = A.left
                else:
                    temp.right = None
                    check(A)
                    A = A.right
        res[0].val, res[-1].val = res[-1].val, res[0].val       
                    
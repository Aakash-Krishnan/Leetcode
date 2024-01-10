# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjMat = defaultdict(list)
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            
            if node.left:
                q.append(node.left)
                adjMat[node.val].append(node.left.val)
                adjMat[node.left.val].append(node.val)
            if node.right:
                q.append(node.right)
                adjMat[node.val].append(node.right.val)
                adjMat[node.right.val].append(node.val)
        
        q = deque()
        q.append((start, 0))
        visited = set()
        visited.add(start)
        
        while q:
            infected, time = q.popleft()
            for neighbour in adjMat[infected]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append((neighbour, time + 1))
        return time
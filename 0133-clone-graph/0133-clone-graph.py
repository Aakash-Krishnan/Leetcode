"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneMap = {}
        
        def dfsClone(node):
            if node in cloneMap:
                return cloneMap[node]
            
            copy = Node(node.val)
            cloneMap[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(dfsClone(nei))
            
            return copy
            
        
        return dfsClone(node) if node else None
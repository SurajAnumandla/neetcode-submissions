"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        freq = {}
        def dfs(node):    
            if not node:
                return
            if node.val in freq:
                return freq[node.val]
            else:
                new_node = Node(node.val)
                freq[node.val] = new_node
                
                for n in node.neighbors:
                    new_node.neighbors.append(dfs(n))
            return new_node
        return dfs(node)
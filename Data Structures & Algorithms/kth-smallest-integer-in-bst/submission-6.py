# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def inorder(self, root,res):
        if root is None:
            return
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.inorder(root,res)
        return res[k-1]
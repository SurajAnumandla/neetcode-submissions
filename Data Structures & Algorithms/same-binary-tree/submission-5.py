# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pre_order(self, root,a):
        if root is None:
            a.append(None)
            return 
        a.append(root.val)
        self.pre_order(root.left,a)
        self.pre_order(root.right,a)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a = []
        b = []
        self.pre_order(p,a)
        self.pre_order(q,b)
        return a==b
        
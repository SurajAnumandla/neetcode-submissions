# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self,root,arr):
        if root is None:
            arr.append(None)
            return 
        arr.append(root.val)
        self.inorder(root.left,arr)
        self.inorder(root.right,arr)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        resp = []
        resq = []
        self.inorder(p,resp)
        self.inorder(q,resq)
        return resp == resq
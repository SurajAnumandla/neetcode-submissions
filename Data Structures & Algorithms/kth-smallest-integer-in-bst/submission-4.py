# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def in_order(self,root,res):
        if root is None:
            return 
        self.in_order(root.left,res)
        res.append(root.val)
        self.in_order(root.right,res)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res= []
        self.in_order(root,res)
        return res[k-1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_same(self,p,q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val!=q.val:
            return False
        left = self.is_same(p.left,q.left)
        right = self.is_same(p.right,q.right)

        return left and right 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> list:
        if root is None:
            return False
        
        if self.is_same(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

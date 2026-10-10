# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validate(self,root, mn, mx):
        if root is None:
            return True 
        if root.val < mn or root.val > mx:
            return False
        left = self.validate(root.left,mn,root.val-1)
        right = self.validate(root.right,root.val+1,mx)
        return left and right 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root,float('-inf'),float('inf'))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkBST(self, root,mn,mx):
        if root is None:
            return True
        if root.val<mn or root.val>mx:
            return False
        checkleft = self.checkBST(root.left,mn,root.val-1)
        checkright = self.checkBST(root.right,root.val+1,mx)

        return checkleft and checkright

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, float('-inf'), float('inf'))
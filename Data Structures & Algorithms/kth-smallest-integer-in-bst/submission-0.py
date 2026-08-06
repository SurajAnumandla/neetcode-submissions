# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = []
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        self.inorder(root)
        return self.res[k-1]
